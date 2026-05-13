# Telegram API и WTelegramClient: идентификаторы и отправка сообщений

Версия: v1. Дата: 2026-03.

## 1. Официальный API: Bot API dialog IDs (core.telegram.org)

Источник: https://core.telegram.org/api/bots/ids

Единый 64‑битный идентификатор пира (user/chat/channel). Хранить в 64‑bit integer или double, не в 32‑bit.

### 1.1 Пользователи (User)

- MTProto user ID: `1` … `0xffffffffff`.
- Bot API = MTProto, конвертация не нужна: `botApiUserId = userId`.

### 1.2 Обычные группы (Chat, basic group)

- MTProto chat ID: `1` … `999999999999`.
- Bot API: **отрицательный** MTProto id.
  - `botApiChatId = -chatId`
  - `chatId = -botApiChatId`
- Диапазон Bot API: `-999999999999` … `-1`.

### 1.3 Супергруппы и каналы (Channel / supergroup)

- MTProto channel ID: общая последовательность `1` … `997852516352`.
- Bot API: сдвиг на 10^12 и минус:
  - `botApiChannelId = -(1000000000000 + channelId)`
  - `channelId = -botApiChannelId - 1000000000000`
- Диапазон Bot API: `-1997852516352` … `-1000000000001`.

Важно: в MTProto супергруппа и канал — один тип (Channel), различаются флагами (megagroup, broadcast). Для обоих в запросах используется **InputPeerChannel(channel_id, access_hash)**; в TL оба поля имеют тип **long** (64‑бит), не int.

### 1.4 Monoforum и секретные чаты

- Monoforum: отдельный диапазон MTProto, формула как у каналов.
- Secret chat: свой диапазон и смещение (см. core.telegram.org).

---

## 2. MTProto: InputPeerChannel и access_hash

- Конструктор (core.telegram.org): `inputPeerChannel#27bcbbfc channel_id:long access_hash:long = InputPeer`.
- **channel_id** и **access_hash** в TL — тип **long**. Не приводить channel_id к int: при channel_id > 2^31 будет переполнение и ошибка CHANNEL_INVALID.
- access_hash берётся из объекта channel (или channelFull) при получении диалогов/чатов; без актуального access_hash запросы к каналу могут отклоняться.

---

## 3. WTelegramClient (C#): два способа работы с чатами

### 3.1 Messages_GetAllDialogs

- Возвращает **все** диалоги: личные чаты, группы, каналы.
- Тип ответа: `Messages_Dialogs` или `Messages_DialogsSlice`; внутри — списки `dialogs`, `chats`, `users`, `messages`.
- В `chats` — объекты `ChatBase` (Chat для обычных групп, Channel для супергрупп/каналов). Ключ в итераторе — id из объекта (для Channel — MTProto channel id).
- Удобно для: полный список диалогов, разбор по типам (User/Chat/Channel). Для отправки в канал/супергруппу нужно самому собрать **InputPeerChannel(channel_id: long, access_hash)** из найденного Channel и не приводить channel_id к int.

### 3.2 Messages_GetAllChats

- Возвращает **только группы и каналы** (без личных диалогов).
- `chats` — словарь: ключ = id чата (формат как в API — см. документацию/примеры библиотеки), значение — `ChatBase` с уже заполненным access_hash.
- Рекомендуемый сценарий отправки: получить чаты → выбрать чат по id → передать **объект ChatBase** в **SendMessageAsync**. Тогда InputPeer собирает сама библиотека, переполнения channel_id не будет.

Пример (из официальных примеров WTelegramClient):

```csharp
var chats = await client.Messages_GetAllChats();
foreach (var (id, chat) in chats.chats)
    if (chat.IsActive)
        Console.WriteLine($"{id,10}: {chat}");
long chatId = long.Parse(Console.ReadLine());
await client.SendMessageAsync(chats.chats[chatId], "Hello, World");
```

Если группа мигрировала в супергруппу, в списке могут быть старый Chat (deactivated) и новый Channel — использовать Channel.

### 3.3 SendMessageAsync

- Сигнатура: отправка по **InputPeer** или по **ChatBase/User** (в зависимости от перегрузки). Безопаснее передавать ChatBase из GetAllChats, чтобы не ошибиться с типом id и не кастить channel_id в int.

---

## 4. Типичные ошибки при своей реализации

1. **Приведение channel_id к int** при создании InputPeerChannel: при channel_id > 2^31 получается неверный id и CHANNEL_INVALID. В TL поле long — передавать long.
2. **Путаница форматов id**: в одном месте использовать «положительный» id вида `1000000000000 - channelId`, в другом — «отрицательный» Bot API `-(1000000000000 + channelId)`. Нужна одна конвенция и явное преобразование в MTProto channel_id при обращении к API.
3. **Использование только GetAllDialogs и ручная сборка InputPeer** вместо GetAllChats + SendMessageAsync(chat): второй путь проще и исключает ошибки с id и access_hash.

---

## 5. Ссылки

- Bot API dialog IDs: https://core.telegram.org/api/bots/ids  
- inputPeerChannel: https://core.telegram.org/constructor/inputPeerChannel  
- Channels/supergroups: https://core.telegram.org/api/channel  
- WTelegramClient: https://github.com/wiz0u/WTelegramClient (EXAMPLES.md, README)  
- Context7 library: /wiz0u/wtelegramclient