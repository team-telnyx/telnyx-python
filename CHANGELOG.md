# Changelog

## 4.110.0 (2026-04-15)

Full Changelog: [v4.109.0...v4.110.0](https://github.com/team-telnyx/telnyx-python/compare/v4.109.0...v4.110.0)

### Features

* MSG-6868: document whitelisted_destinations as conditionally required ([ceaaffb](https://github.com/team-telnyx/telnyx-python/commit/ceaaffb4f9d116f57d5b5fe96554acb2c96eea08))

## 4.109.0 (2026-04-14)

Full Changelog: [v4.108.0...v4.109.0](https://github.com/team-telnyx/telnyx-python/compare/v4.108.0...v4.109.0)

### Features

* TELAPPS-5712: Add deepfake detection to call-control API spec ([a645d7e](https://github.com/team-telnyx/telnyx-python/commit/a645d7efa72197125e8bd7b71c2a70754be92d7e))

## 4.108.0 (2026-04-13)

Full Changelog: [v4.107.0...v4.108.0](https://github.com/team-telnyx/telnyx-python/compare/v4.107.0...v4.108.0)

### Features

* [TDA-6425] Fix session analysis API spec: relaxed date_time, remove status & completed_at ([93c33c4](https://github.com/team-telnyx/telnyx-python/commit/93c33c471f0221026f65e411ac34ca14b360175d))

## 4.107.0 (2026-04-13)

Full Changelog: [v4.106.0...v4.107.0](https://github.com/team-telnyx/telnyx-python/compare/v4.106.0...v4.107.0)

### Features

* **client:** allow enqueuing to websockets even when not connected ([5878b59](https://github.com/team-telnyx/telnyx-python/commit/5878b59e47bab464ad7d17e1b658a7869303642a))

## 4.106.0 (2026-04-13)

Full Changelog: [v4.105.1...v4.106.0](https://github.com/team-telnyx/telnyx-python/compare/v4.105.1...v4.106.0)

### Features

* Add webhook_urls, webhook_urls_method, webhook_retries_policies to Dial endpoint ([eaa792a](https://github.com/team-telnyx/telnyx-python/commit/eaa792a19419987b458d06abcf0174ba51e3d198))

## 4.105.1 (2026-04-12)

Full Changelog: [v4.105.0...v4.105.1](https://github.com/team-telnyx/telnyx-python/compare/v4.105.0...v4.105.1)

### Bug Fixes

* set additionalProperties=false on VoiceCloneUploadRequest to prevent codegen errors ([b4e8552](https://github.com/team-telnyx/telnyx-python/commit/b4e8552574460926bbcf98ba3cc0a328f9e5cedd))

## 4.105.0 (2026-04-11)

Full Changelog: [v4.104.1...v4.105.0](https://github.com/team-telnyx/telnyx-python/compare/v4.104.1...v4.105.0)

### Features

* **api:** manual updates ([143b22e](https://github.com/team-telnyx/telnyx-python/commit/143b22e1d3a24c65aab638bcb868f5dfcd940549))
* **client:** add event handler implementation for websockets ([137bcc6](https://github.com/team-telnyx/telnyx-python/commit/137bcc63bc09f9a01e958a463a42144d46726e65))
* **lib:** make ED25519 the default webhook verification ([5116ac8](https://github.com/team-telnyx/telnyx-python/commit/5116ac876f2a99d3664d59d2ee9bf50a0c9c3387))


### Bug Fixes

* resolve pyright type error in text_to_speech event handler ([e209866](https://github.com/team-telnyx/telnyx-python/commit/e209866009201d11ac5aabaf49bfe66cb67ec885))


### Documentation

* improve examples ([4e53d34](https://github.com/team-telnyx/telnyx-python/commit/4e53d34555a18b433d5f5eff075057387fd5ecb7))

## 4.104.1 (2026-04-10)

Full Changelog: [v4.104.0...v4.104.1](https://github.com/team-telnyx/telnyx-python/compare/v4.104.0...v4.104.1)

### Bug Fixes

* ensure file data are only sent as 1 parameter ([f0cb6ac](https://github.com/team-telnyx/telnyx-python/commit/f0cb6ac811a97399d137852b207e3b18822297b1))

## 4.104.0 (2026-04-10)

Full Changelog: [v4.103.0...v4.104.0](https://github.com/team-telnyx/telnyx-python/compare/v4.103.0...v4.104.0)

### Features

* **api:** Merge pull request [#46](https://github.com/team-telnyx/telnyx-python/issues/46) from stainless-sdks/FixModelRecommendation ([911071c](https://github.com/team-telnyx/telnyx-python/commit/911071c8cf4c85514d0730be91dbb93d65a61ebf))

## 4.103.0 (2026-04-10)

Full Changelog: [v4.102.0...v4.103.0](https://github.com/team-telnyx/telnyx-python/compare/v4.102.0...v4.103.0)

### Features

* MSG-6846: add GET /profile/photo docs for whatsapp API ([47e8f01](https://github.com/team-telnyx/telnyx-python/commit/47e8f018531b5c4a702e5185e144df004fe7cfab))


### Reverts

* restore stainless.yml to pre-6a6df5b state ([4f9838b](https://github.com/team-telnyx/telnyx-python/commit/4f9838bfc30b134a842f4313ea784121821b31c7))

## 4.102.0 (2026-04-09)

Full Changelog: [v4.101.0...v4.102.0](https://github.com/team-telnyx/telnyx-python/compare/v4.101.0...v4.102.0)

### Features

* add shared CallAssistantRequest schema for call-control assistant object ([b24aecf](https://github.com/team-telnyx/telnyx-python/commit/b24aecff912822fadd885d4be7319b2817d48a95))

## 4.101.0 (2026-04-09)

Full Changelog: [v4.100.0...v4.101.0](https://github.com/team-telnyx/telnyx-python/compare/v4.100.0...v4.101.0)

### Features

* **api:** Merge pull request [#44](https://github.com/team-telnyx/telnyx-python/issues/44) from stainless-sdks/fix-NameNotAllowed ([a19231b](https://github.com/team-telnyx/telnyx-python/commit/a19231bd8d47f96fbf45dde2b87adf588522a3e7))

## 4.100.0 (2026-04-09)

Full Changelog: [v4.99.0...v4.100.0](https://github.com/team-telnyx/telnyx-python/compare/v4.99.0...v4.100.0)

### Features

* **client:** support reconnection in websockets ([4f8ca17](https://github.com/team-telnyx/telnyx-python/commit/4f8ca177181fe2c0747bdd045356f7841b70690f))


### Reverts

* revert stainless.yml changes from 9c5e8d8 ([9930faa](https://github.com/team-telnyx/telnyx-python/commit/9930faa7d2d54bb6b50e100c6fbfb96bea0a1043))


### Documentation

* update voice clone schemas to match Ultra/model_id implementation ([f370dde](https://github.com/team-telnyx/telnyx-python/commit/f370dde4582bfe7714d7efc8be3571028a8cf7aa))

## 4.99.0 (2026-04-08)

Full Changelog: [v4.98.0...v4.99.0](https://github.com/team-telnyx/telnyx-python/compare/v4.98.0...v4.99.0)

### Features

* TELAPPS-5707: Add privacy parameter to Call Control dial and transfer ([994a4ae](https://github.com/team-telnyx/telnyx-python/commit/994a4ae45ea23d56e53d9b63c0900ff194579b81))


### Reverts

* revert stainless.yml changes from pronunciation dictionaries commit ([62f4c82](https://github.com/team-telnyx/telnyx-python/commit/62f4c82b7231098bac5254a4a4ae05ec0c5550a4))

## 4.98.0 (2026-04-08)

Full Changelog: [v4.97.0...v4.98.0](https://github.com/team-telnyx/telnyx-python/compare/v4.97.0...v4.98.0)

### Features

* TELAPPS-5689: Pronunciation dictionaries API docs ([eb1bebf](https://github.com/team-telnyx/telnyx-python/commit/eb1bebfd40a114d54025e1b151f28d55de88ffa6))

## 4.97.0 (2026-04-08)

Full Changelog: [v4.96.0...v4.97.0](https://github.com/team-telnyx/telnyx-python/compare/v4.96.0...v4.97.0)

### Features

* Add ai_calls endpoint documentation to OpenAPI spec ([586c445](https://github.com/team-telnyx/telnyx-python/commit/586c44557cec717765f9aff0e7f67b4f81a2d50a))
* Add oneOf constraint for Url/Texml mutual exclusivity in InitiateCallRequest ([a444d3a](https://github.com/team-telnyx/telnyx-python/commit/a444d3a66987f8d6625e3dbce7ab69625e21e7ae))
* **api:** Merge pull request [#39](https://github.com/team-telnyx/telnyx-python/issues/39) from stainless-sdks/revert-a988c49-stainless-changes ([75ee85b](https://github.com/team-telnyx/telnyx-python/commit/75ee85b1f03acee3d5a759ab13503c8ac5da729b))
* **client:** support sending raw data over websockets ([f475022](https://github.com/team-telnyx/telnyx-python/commit/f4750222c54658dfa0e2a43bc54758e7128f6275))
* CW-3815 fix PATCH /wirelss_blocklists/{id} endpoint ([5b7eb9f](https://github.com/team-telnyx/telnyx-python/commit/5b7eb9f2335152f2ba68a4a06c578e95761b6c41))


### Reverts

* restore stainless.yml SDK generation fixes ([75ee85b](https://github.com/team-telnyx/telnyx-python/commit/75ee85b1f03acee3d5a759ab13503c8ac5da729b))

## 4.96.0 (2026-04-07)

Full Changelog: [v4.95.0...v4.96.0](https://github.com/team-telnyx/telnyx-python/compare/v4.95.0...v4.96.0)

### Features

* AI-2180: Add message_template to SendMessageTool schema ([7e21d03](https://github.com/team-telnyx/telnyx-python/commit/7e21d03c66deab58fdad063a0f9b2b14805576d2))

## 4.95.0 (2026-04-07)

Full Changelog: [v4.94.1...v4.95.0](https://github.com/team-telnyx/telnyx-python/compare/v4.94.1...v4.95.0)

### Features

* add enabled boolean to recording_settings [AI-2178] ([0c7505a](https://github.com/team-telnyx/telnyx-python/commit/0c7505a6f76751c5a88fa715624f554be6325a80))

## 4.94.1 (2026-04-07)

Full Changelog: [v4.94.0...v4.94.1](https://github.com/team-telnyx/telnyx-python/compare/v4.94.0...v4.94.1)

### Bug Fixes

* **client:** preserve hardcoded query params when merging with user params ([acc1ed8](https://github.com/team-telnyx/telnyx-python/commit/acc1ed8681f91c7f601916c297dc2fa0a4b59617))

## 4.94.0 (2026-04-07)

Full Changelog: [v4.93.0...v4.94.0](https://github.com/team-telnyx/telnyx-python/compare/v4.93.0...v4.94.0)

### Features

* **api:** manual updates ([16342a1](https://github.com/team-telnyx/telnyx-python/commit/16342a1b12cb9b1bd14b03cb54023defcf105a96))

## 4.93.0 (2026-04-07)

Full Changelog: [v4.92.0...v4.93.0](https://github.com/team-telnyx/telnyx-python/compare/v4.92.0...v4.93.0)

### Features

* MSG-6666: Add template and text properties to WhatsApp send message schema ([313ba3d](https://github.com/team-telnyx/telnyx-python/commit/313ba3d602d43079854e8b8dc8ee8a68c8cf5c47))

## 4.92.0 (2026-04-07)

Full Changelog: [v4.91.0...v4.92.0](https://github.com/team-telnyx/telnyx-python/compare/v4.91.0...v4.92.0)

### Features

* Assistants: add observability ([0782eea](https://github.com/team-telnyx/telnyx-python/commit/0782eeabd629a5178d4db6ace324398c5b9b6094))

## 4.91.0 (2026-04-07)

Full Changelog: [v4.90.0...v4.91.0](https://github.com/team-telnyx/telnyx-python/compare/v4.90.0...v4.91.0)

### Features

* MSG-6673: Add WhatsApp verification endpoint and profile settings ([e873736](https://github.com/team-telnyx/telnyx-python/commit/e8737361ace9db26d4f9e89ed79ceada7c89caa8))

## 4.90.0 (2026-03-31)

Full Changelog: [v4.89.0...v4.90.0](https://github.com/team-telnyx/telnyx-python/compare/v4.89.0...v4.90.0)

### Features

* **lib:** add ED25519 webhook signature verification ([18be54b](https://github.com/team-telnyx/telnyx-python/commit/18be54bff12109ba79b6ba2a80a881fdfaa523f0))

## 4.89.0 (2026-03-30)

Full Changelog: [v4.88.1...v4.89.0](https://github.com/team-telnyx/telnyx-python/compare/v4.88.1...v4.89.0)

### Features

* **lib:** add Speech-to-Text WebSocket streaming support ([b7e059a](https://github.com/team-telnyx/telnyx-python/commit/b7e059ab7d86a982f8773a420867f827fde2ca51))


### Bug Fixes

* resolve pyright strict mode type errors ([3283d71](https://github.com/team-telnyx/telnyx-python/commit/3283d71d81d515147e7c2b96acf541f38ae34f9c))
* resolve ruff import sorting errors ([f210455](https://github.com/team-telnyx/telnyx-python/commit/f2104551e00dedd2db3bab6596e58591efd899ef))

## 4.88.1 (2026-03-28)

Full Changelog: [v4.88.0...v4.88.1](https://github.com/team-telnyx/telnyx-python/compare/v4.88.0...v4.88.1)

### Bug Fixes

* **python:** add edition python.2025-11-20 for OIDC support ([018532e](https://github.com/team-telnyx/telnyx-python/commit/018532e7217cd1a3b03530b76d84a9f9d2302528))


### Chores

* sync repo ([a70b9c2](https://github.com/team-telnyx/telnyx-python/commit/a70b9c2922e4196876a3c68057e461c63cc44f5f))
