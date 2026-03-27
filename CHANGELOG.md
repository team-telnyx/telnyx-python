# Changelog

## 4.87.1 (2026-03-27)

Full Changelog: [v4.87.0...v4.87.1](https://github.com/team-telnyx/telnyx-python/compare/v4.87.0...v4.87.1)

### Chores

* **ci:** use oidc publishing ([eeda30a](https://github.com/team-telnyx/telnyx-python/commit/eeda30aa1936b6c33d22bc9352c68ee913730aa9))


### Documentation

* fix voice settings available voices link ([d391407](https://github.com/team-telnyx/telnyx-python/commit/d3914074bb98405f62ebd41b5272616c7c8e530f))

## 4.87.0 (2026-03-26)

Full Changelog: [v4.86.1...v4.87.0](https://github.com/team-telnyx/telnyx-python/compare/v4.86.1...v4.87.0)

### Features

* **internal:** implement indices array format for query and form serialization ([1de2959](https://github.com/team-telnyx/telnyx-python/commit/1de295920ee04d3f4cbe4984d76eef1c9eba7841))

## 4.86.1 (2026-03-25)

Full Changelog: [v4.86.0...v4.86.1](https://github.com/team-telnyx/telnyx-python/compare/v4.86.0...v4.86.1)

### Bug Fixes

* rename number-reputation ToS route to use underscores ([df56464](https://github.com/team-telnyx/telnyx-python/commit/df5646407c6e651bf08dff99e2359d079ba9d83c))


### Documentation

* **branded-calling:** add Number Reputation API specs ([cebfcf3](https://github.com/team-telnyx/telnyx-python/commit/cebfcf3e9fe7cc5ad8b20be921ddf839aeb81ea7))

## 4.86.0 (2026-03-24)

Full Changelog: [v4.85.0...v4.86.0](https://github.com/team-telnyx/telnyx-python/compare/v4.85.0...v4.86.0)

### Features

* New tools api ([568023f](https://github.com/team-telnyx/telnyx-python/commit/568023f75797bf08f172d5655bbc8031fc9f1048))

## 4.85.0 (2026-03-24)

Full Changelog: [v4.84.0...v4.85.0](https://github.com/team-telnyx/telnyx-python/compare/v4.84.0...v4.85.0)

### Features

* TELAPPS-5685: Add store_fields_as_variables to WebhookToolParams ([7e22baa](https://github.com/team-telnyx/telnyx-python/commit/7e22baa225cb2e4ae8695ffc51bd9f5eb7fa2df4))

## 4.84.0 (2026-03-24)

Full Changelog: [v4.83.0...v4.84.0](https://github.com/team-telnyx/telnyx-python/compare/v4.83.0...v4.84.0)

### Features

* **api:** Merge pull request [#30](https://github.com/team-telnyx/telnyx-python/issues/30) from stainless-sdks/fix-schemaUnionDiscriminatorMissing ([0fb60ae](https://github.com/team-telnyx/telnyx-python/commit/0fb60ae4db579b458cb30b1ece6a27dd1f0dff61))


### Chores

* **ci:** skip lint on metadata-only changes ([6a26d79](https://github.com/team-telnyx/telnyx-python/commit/6a26d79d236777735707f0ce7ac93eb1e90d260f))
* **internal:** update gitignore ([9b892a4](https://github.com/team-telnyx/telnyx-python/commit/9b892a4c5a1781278d768d09e61f51cbb56f1a63))

## 4.83.0 (2026-03-23)

Full Changelog: [v4.82.0...v4.83.0](https://github.com/team-telnyx/telnyx-python/compare/v4.82.0...v4.83.0)

### Features

* **api:** manual updates ([9f7eed7](https://github.com/team-telnyx/telnyx-python/commit/9f7eed7bfd09a5fa86344e333bdb0909fb59b7e7))


### Documentation

* WhatsApp template components schema ([01a856a](https://github.com/team-telnyx/telnyx-python/commit/01a856ab64e3074a7799485e3ef5e52aa77534d7))

## 4.82.0 (2026-03-20)

Full Changelog: [v4.81.1...v4.82.0](https://github.com/team-telnyx/telnyx-python/compare/v4.81.1...v4.82.0)

### Features

* Add Minimax provider support to Voice Designs and Voice Clones API spec ([3c69d56](https://github.com/team-telnyx/telnyx-python/commit/3c69d560962b499eccaeae70d6882b28c2e64ab4))
* **api:** manual updates ([b0edd56](https://github.com/team-telnyx/telnyx-python/commit/b0edd56c61ea53bf8e294736dd823b70313d9f66))


### Bug Fixes

* correct x402 resource return types ([da227d0](https://github.com/team-telnyx/telnyx-python/commit/da227d0e36a8c5810b71396ea4be2dcc214f2ff9))

## 4.81.1 (2026-03-20)

Full Changelog: [v4.81.0...v4.81.1](https://github.com/team-telnyx/telnyx-python/compare/v4.81.0...v4.81.1)

### Bug Fixes

* correct import ordering for lint ([0518d88](https://github.com/team-telnyx/telnyx-python/commit/0518d885648472dfe8b555938cb0a97523dc3492))
* import TelnyxWebhookVerificationError from lib module in resources/__init__.py ([2b92532](https://github.com/team-telnyx/telnyx-python/commit/2b92532a56c1bc577285bf1b02591e44bcb5849d))
* sort imports to pass lint ([46e7b6c](https://github.com/team-telnyx/telnyx-python/commit/46e7b6c59df06da8781225bb599c40183a625135))


### Refactors

* move webhook verification to separate module to avoid merge conflicts ([230a1ac](https://github.com/team-telnyx/telnyx-python/commit/230a1ac3d1deaa002b010c6409b29ec1afd5117b))

## 4.81.0 (2026-03-19)

Full Changelog: [v4.80.0...v4.81.0](https://github.com/team-telnyx/telnyx-python/compare/v4.80.0...v4.81.0)

### Features

* add HTTP transcribe() method to speech_to_text for parity with TypeScript ([220736f](https://github.com/team-telnyx/telnyx-python/commit/220736fc369291d635a68a3b35925772b418cb12))
* **api:** manual updates ([7a1dfe2](https://github.com/team-telnyx/telnyx-python/commit/7a1dfe2bc46d2c85943fd05ca1cb6450218b3fb7))
* **api:** manual updates ([5e54b72](https://github.com/team-telnyx/telnyx-python/commit/5e54b7254155eaea4161362474bf8ad69068d6ea))
* **api:** manual updates ([581ee71](https://github.com/team-telnyx/telnyx-python/commit/581ee7158875c7253fc19e4e91bca3beb301acf4))
* TELAPPS-5668: Add call.cost webhook event documentation ([ae53676](https://github.com/team-telnyx/telnyx-python/commit/ae53676a72faec983bff7d78d42e73ee5c604ae2))
* **wireless:** add traffic policy profiles endpoints to OpenAPI spec ([e1f00fd](https://github.com/team-telnyx/telnyx-python/commit/e1f00fd22cef573bd63ce187af733ca160a405fb))


### Bug Fixes

* restore deleted modules for speech_to_text, text_to_speech, and whatsapp_message_templates ([275701d](https://github.com/team-telnyx/telnyx-python/commit/275701da2c8cdd25c2b1acd9936dbaf410eb03cc))
* sanitize endpoint path params ([a0143f2](https://github.com/team-telnyx/telnyx-python/commit/a0143f23dbda5147750b0248c4c28023a1cc49f8))


### Documentation

* **tts:** Add Telnyx.Ultra model documentation ([3059e3e](https://github.com/team-telnyx/telnyx-python/commit/3059e3ebfcba108c779aeb2b179a44078ac3117c))

## 4.80.0 (2026-03-18)

Full Changelog: [v4.79.0...v4.80.0](https://github.com/team-telnyx/telnyx-python/compare/v4.79.0...v4.80.0)

### Features

* **api:** manual updates ([bacb42c](https://github.com/team-telnyx/telnyx-python/commit/bacb42cda955b825721e4ea5dc1e2763b1f041b7))

## 4.79.0 (2026-03-18)

Full Changelog: [v4.78.0...v4.79.0](https://github.com/team-telnyx/telnyx-python/compare/v4.78.0...v4.79.0)

### Features

* add message_history, send_message_history_updates, participants to AIAssistantStartRequest ([cd521f0](https://github.com/team-telnyx/telnyx-python/commit/cd521f0b00758bda9ed3581f4499c7c18d4a26cc))

## 4.78.0 (2026-03-18)

Full Changelog: [v4.77.0...v4.78.0](https://github.com/team-telnyx/telnyx-python/compare/v4.77.0...v4.78.0)

### Features

* port-4690: fix LOA configuration preview path (singular → plural) ([a6c9af8](https://github.com/team-telnyx/telnyx-python/commit/a6c9af8bb6500612a6f2bddae9bda84757918d3f))

## 4.77.0 (2026-03-18)

Full Changelog: [v4.76.0...v4.77.0](https://github.com/team-telnyx/telnyx-python/compare/v4.76.0...v4.77.0)

### Features

* add ai_assistant_join call control command OpenAPI spec ([6276857](https://github.com/team-telnyx/telnyx-python/commit/627685730e0f148296d48310383e92f4173dec30))


### Bug Fixes

* revert generated tests for WebSocket stream methods ([e20a0e8](https://github.com/team-telnyx/telnyx-python/commit/e20a0e8461ad2ab85bea25223be3bad14a0d4f0a))

## 4.76.0 (2026-03-16)

Full Changelog: [v4.75.2...v4.76.0](https://github.com/team-telnyx/telnyx-python/compare/v4.75.2...v4.76.0)

### Features

* CW-2881 update `filter[action_type]` enum ([18dc08f](https://github.com/team-telnyx/telnyx-python/commit/18dc08ffc05d58be686e93566f2e4c715eba2fd2))


### Chores

* **internal:** tweak CI branches ([ef46d7f](https://github.com/team-telnyx/telnyx-python/commit/ef46d7fb6c7aced9d3585f237d4a7f04441109e0))

## 4.75.2 (2026-03-16)

Full Changelog: [v4.75.1...v4.75.2](https://github.com/team-telnyx/telnyx-python/compare/v4.75.1...v4.75.2)

### Bug Fixes

* **deps:** bump minimum typing-extensions version ([a2dd1ec](https://github.com/team-telnyx/telnyx-python/commit/a2dd1eccb763e114f494130aef759ad88c04b2e8))

## 4.75.1 (2026-03-16)

Full Changelog: [v4.75.0...v4.75.1](https://github.com/team-telnyx/telnyx-python/compare/v4.75.0...v4.75.1)

### Bug Fixes

* **pydantic:** do not pass `by_alias` unless set ([56b3cfb](https://github.com/team-telnyx/telnyx-python/commit/56b3cfbccecc81e253103fcc4b2578bd4d248ddb))

## 4.75.0 (2026-03-16)

Full Changelog: [v4.74.0...v4.75.0](https://github.com/team-telnyx/telnyx-python/compare/v4.74.0...v4.75.0)

### Features

* AI-2132: Add warm_message_delay_ms to transfer tool OpenAPI spec ([b17ff61](https://github.com/team-telnyx/telnyx-python/commit/b17ff61b79cee1bf5f6d9c34969a5b9c11c1bff0))

## 4.74.0 (2026-03-13)

Full Changelog: [v4.73.0...v4.74.0](https://github.com/team-telnyx/telnyx-python/compare/v4.73.0...v4.74.0)

### Features

* AI-2131: Add expressive_mode boolean to VoiceSettings ([aca3c72](https://github.com/team-telnyx/telnyx-python/commit/aca3c728a11e448978403209b916b88825833382))

## 4.73.0 (2026-03-13)

Full Changelog: [v4.72.0...v4.73.0](https://github.com/team-telnyx/telnyx-python/compare/v4.72.0...v4.73.0)

### Features

* **api:** manual updates ([25472c4](https://github.com/team-telnyx/telnyx-python/commit/25472c48a8a6a688a8c3bf53b70d553379b171a9))

## 4.72.0 (2026-03-13)

Full Changelog: [v4.71.3...v4.72.0](https://github.com/team-telnyx/telnyx-python/compare/v4.71.3...v4.72.0)

### Features

* add public x402 payment endpoints to external specs ([5c45180](https://github.com/team-telnyx/telnyx-python/commit/5c45180ab8176b08cb848eea74b58e865710e167))

## 4.71.3 (2026-03-13)

Full Changelog: [v4.71.2...v4.71.3](https://github.com/team-telnyx/telnyx-python/compare/v4.71.2...v4.71.3)

### Bug Fixes

* **call-recordings:** align OpenAPI spec with implementation ([ba44a14](https://github.com/team-telnyx/telnyx-python/commit/ba44a1442504e070d10f4d2a2c281f166148b582))

## 4.71.2 (2026-03-13)

Full Changelog: [v4.71.1...v4.71.2](https://github.com/team-telnyx/telnyx-python/compare/v4.71.1...v4.71.2)

### Bug Fixes

* lint errors in _client.py ([08e1685](https://github.com/team-telnyx/telnyx-python/commit/08e1685411873c189db33fcb8c2b041040b4ecf9))
* update WebsocketConnectionOptions -&gt; WebSocketConnectionOptions ([714eb76](https://github.com/team-telnyx/telnyx-python/commit/714eb76e7767d2e86e83e169a3273b1357a291ec))
* wire up SpeechToTextResource to client ([762f42d](https://github.com/team-telnyx/telnyx-python/commit/762f42da6de8cc071bce18db39a4dcdcda964216))

## 4.71.1 (2026-03-13)

Full Changelog: [v4.71.0...v4.71.1](https://github.com/team-telnyx/telnyx-python/compare/v4.71.0...v4.71.1)

### Bug Fixes

* **tests:** correct setup of OAuth 2 Client Credentials tests ([c8bfd0f](https://github.com/team-telnyx/telnyx-python/commit/c8bfd0ff91387363ccbd91847f00e83cb26becf8))

## 4.71.0 (2026-03-13)

Full Changelog: [v4.70.0...v4.71.0](https://github.com/team-telnyx/telnyx-python/compare/v4.70.0...v4.71.0)

### Features

* **api:** Merge pull request [#29](https://github.com/team-telnyx/telnyx-python/issues/29) from stainless-sdks/fix-add-voice-model ([167cbf2](https://github.com/team-telnyx/telnyx-python/commit/167cbf265f2772ec41acdf41f80982465060f36a))
* **api:** update OpenAPI spec or Stainless config ([167cbf2](https://github.com/team-telnyx/telnyx-python/commit/167cbf265f2772ec41acdf41f80982465060f36a))

## 4.70.0 (2026-03-12)

Full Changelog: [v4.69.1...v4.70.0](https://github.com/team-telnyx/telnyx-python/compare/v4.69.1...v4.70.0)

### Features

* Add Voice Designs and Voice Clones API specification ([3300a21](https://github.com/team-telnyx/telnyx-python/commit/3300a211cd0aebc7aee9fa50447ee91a17e9865d))


### Reverts

* restore stainless.yml changes removed in 1de6067 ([9a71770](https://github.com/team-telnyx/telnyx-python/commit/9a7177016ec5071291e77b593da1d61f7d9e4a0b))


### Chores

* update example date in usage-reports ([c026d4e](https://github.com/team-telnyx/telnyx-python/commit/c026d4edf91b5ab2102a14acf98c1ed6633c3196))

## 4.69.1 (2026-03-11)

Full Changelog: [v4.69.0...v4.69.1](https://github.com/team-telnyx/telnyx-python/compare/v4.69.0...v4.69.1)

### Bug Fixes

* add missing vertical enum values for 10DLC brand creation (ENGDESK-49040) ([5675e18](https://github.com/team-telnyx/telnyx-python/commit/5675e185c763e5d35d1b79d8971488136198757b))

## 4.69.0 (2026-03-11)

Full Changelog: [v4.68.0...v4.69.0](https://github.com/team-telnyx/telnyx-python/compare/v4.68.0...v4.69.0)

### Features

* **api:** manual updates ([3a376ee](https://github.com/team-telnyx/telnyx-python/commit/3a376eed66a283b8bb84c59cc13f0aafab9ec936))

## 4.68.0 (2026-03-11)

Full Changelog: [v4.67.0...v4.68.0](https://github.com/team-telnyx/telnyx-python/compare/v4.67.0...v4.68.0)

### Features

* **api:** manual updates ([48eae87](https://github.com/team-telnyx/telnyx-python/commit/48eae877f964011623e9184ff732fb3bb8024e6e))


### Chores

* use proper capitalization for WebSockets ([eb0c4b3](https://github.com/team-telnyx/telnyx-python/commit/eb0c4b3b11ad49cfbe9c14f075bbb003bf2df030))

## 4.67.0 (2026-03-11)

Full Changelog: [v4.66.0...v4.67.0](https://github.com/team-telnyx/telnyx-python/compare/v4.66.0...v4.67.0)

### Features

* **api:** Merge pull request [#27](https://github.com/team-telnyx/telnyx-python/issues/27) from stainless-sdks/fix/whatsapp-message-templates-conflict ([b613738](https://github.com/team-telnyx/telnyx-python/commit/b61373874d712d9814829dc3b3f3e653333e7d8b))


### Bug Fixes

* rename whatsapp.message_templates to whatsapp.templates to avoid conflict ([b613738](https://github.com/team-telnyx/telnyx-python/commit/b61373874d712d9814829dc3b3f3e653333e7d8b))

## 4.66.0 (2026-03-11)

Full Changelog: [v4.65.2...v4.66.0](https://github.com/team-telnyx/telnyx-python/compare/v4.65.2...v4.66.0)

### Features

* Add enable_thinking parameter to chat completions API ([15b1b8a](https://github.com/team-telnyx/telnyx-python/commit/15b1b8abf3a47641cf80e19d50ce5ffea380c9ec))

## 4.65.2 (2026-03-11)

Full Changelog: [v4.65.1...v4.65.2](https://github.com/team-telnyx/telnyx-python/compare/v4.65.1...v4.65.2)

### Bug Fixes

* update wait_seconds example to 0.5 ([2856cc7](https://github.com/team-telnyx/telnyx-python/commit/2856cc7db119ec997d61b9facbf157886eb30622))


### Chores

* match http protocol with ws protocol instead of wss ([3b84dee](https://github.com/team-telnyx/telnyx-python/commit/3b84dee5902e226c0c80dbdc6bc9875850ff1cdf))

## 4.65.1 (2026-03-11)

Full Changelog: [v4.65.0...v4.65.1](https://github.com/team-telnyx/telnyx-python/compare/v4.65.0...v4.65.1)

## 4.65.0 (2026-03-10)

Full Changelog: [v4.64.1...v4.65.0](https://github.com/team-telnyx/telnyx-python/compare/v4.64.1...v4.65.0)

### Features

* **api:** manual updates ([9f6a891](https://github.com/team-telnyx/telnyx-python/commit/9f6a8911845dc01e3910d9adfa8d7c87a9a7e5dd))

## 4.64.1 (2026-03-10)

Full Changelog: [v4.64.0...v4.64.1](https://github.com/team-telnyx/telnyx-python/compare/v4.64.0...v4.64.1)

### Bug Fixes

* add title to InviteTool.invite for Stainless SDK ([2effda1](https://github.com/team-telnyx/telnyx-python/commit/2effda196419c1331af9f2585a59ff3d7abf2ef6))

## 4.64.0 (2026-03-10)

Full Changelog: [v4.63.0...v4.64.0](https://github.com/team-telnyx/telnyx-python/compare/v4.63.0...v4.64.0)

### Features

* **messaging:** add wait_seconds to OutboundMessagePayload example ([14209ab](https://github.com/team-telnyx/telnyx-python/commit/14209abf6b3f8a444eb85dbb017f7765b982a70e))

## 4.63.0 (2026-03-10)

Full Changelog: [v4.62.0...v4.63.0](https://github.com/team-telnyx/telnyx-python/compare/v4.62.0...v4.63.0)

### Features

* **api:** manual updates ([4d21651](https://github.com/team-telnyx/telnyx-python/commit/4d21651ca9a0095ccea23ef8786b1c28131551a5))

## 4.62.0 (2026-03-10)

Full Changelog: [v4.61.0...v4.62.0](https://github.com/team-telnyx/telnyx-python/compare/v4.61.0...v4.62.0)

### Features

* CW-2881 publish wireless VoLTE docs to prod ([3680bf6](https://github.com/team-telnyx/telnyx-python/commit/3680bf648091513b1a9aa329944a6b178a317f26))

## 4.61.0 (2026-03-09)

Full Changelog: [v4.60.0...v4.61.0](https://github.com/team-telnyx/telnyx-python/compare/v4.60.0...v4.61.0)

### Features

* [TDA-6425] Add Session Analysis API spec to public docs ([a3df3b8](https://github.com/team-telnyx/telnyx-python/commit/a3df3b843527922682335f52396ac6dd2228b8f1))
* AI-2106: Add invite tool schema to inference OpenAPI spec ([7ce2e19](https://github.com/team-telnyx/telnyx-python/commit/7ce2e198c8868461a61c687f0205c0bfe97efd07))
* **api:** manual updates ([307eccb](https://github.com/team-telnyx/telnyx-python/commit/307eccb81f08aac682df5f11a76957f2312e3b14))
* **api:** manual updates ([9836102](https://github.com/team-telnyx/telnyx-python/commit/9836102e8c36049094e466831035378402d66737))
* **api:** manual updates ([fc35872](https://github.com/team-telnyx/telnyx-python/commit/fc35872ea3bae91b1a827b96e3e71d383681a1ab))
* **api:** manual updates ([3685080](https://github.com/team-telnyx/telnyx-python/commit/368508027b9d03b4556ee603ba04f08e8d554a4b))
* **api:** manual updates ([8a92529](https://github.com/team-telnyx/telnyx-python/commit/8a925296430de78be1f5251a2cb2e593d05b8be8))
* **api:** manual updates ([df9980b](https://github.com/team-telnyx/telnyx-python/commit/df9980bf506f4bf1dd84ce83ccc96de84196ba58))
* Assistant tags ([beb4319](https://github.com/team-telnyx/telnyx-python/commit/beb43199a47ebf11b154e22994cbb44c5bb08ce5))
* Changing a tag for filebased STT endpoint ([586a5c9](https://github.com/team-telnyx/telnyx-python/commit/586a5c907c161c1bd2e3680cbb4c0d6564bdeb3d))
* Changing the tag for TTS endpoint ([0f216f6](https://github.com/team-telnyx/telnyx-python/commit/0f216f6df35030b528459c2c33a30f14f67ed9a5))
* MSG-6418: remove flashcall from hosted number verification codes endpoint ([99ea516](https://github.com/team-telnyx/telnyx-python/commit/99ea51685271b53f950114be6d6ffbe42f53aabd))
* **stt:** add WebSocket event schemas for Stainless SDK generation ([834c8f3](https://github.com/team-telnyx/telnyx-python/commit/834c8f33fba5dfbb971cbe343dd92bb0ed11360b))
* TELAPPS-ENGDESK-49737 Add prevent_double_bridge param to dial ([174bb17](https://github.com/team-telnyx/telnyx-python/commit/174bb172c448f52f16fefafff94417dfaf2e1866))


### Bug Fixes

* add discriminator to TtsServerEvent for Stainless SDK generation ([4bec629](https://github.com/team-telnyx/telnyx-python/commit/4bec629443e8d6a2dcfd16ee1c2826908e5d71f6))


### Chores

* **ci:** skip uploading artifacts on stainless-internal branches ([8ccd7b5](https://github.com/team-telnyx/telnyx-python/commit/8ccd7b5af7a8dd54e6ee8f7bc4d36a70350205fe))
* **tests:** update webhook tests ([2578581](https://github.com/team-telnyx/telnyx-python/commit/257858104b910f7c2fc63111641f3d924d49d56e))
* update placeholder string ([5ed11f3](https://github.com/team-telnyx/telnyx-python/commit/5ed11f39762e042a744c5c33761a05b5d9570014))


### Documentation

* **messaging:** Add wait_seconds to message response schemas ([aa938dd](https://github.com/team-telnyx/telnyx-python/commit/aa938ddaeb95691d2d85c85b42b09ab15546eabc))


### Refactors

* **types:** use `extra_items` from PEP 728 ([b5e0ea6](https://github.com/team-telnyx/telnyx-python/commit/b5e0ea620a758d7c9b2be5d77d066d7d83e59001))

## 4.60.0 (2026-03-02)

Full Changelog: [v4.59.1...v4.60.0](https://github.com/team-telnyx/telnyx-python/compare/v4.59.1...v4.60.0)

### Features

* Merge TTS file-based spec into text-to-speech.json ([164d1de](https://github.com/team-telnyx/telnyx-python/commit/164d1ded20e728b49c5a53dfd772858a1e1eb13e))

## 4.59.1 (2026-03-02)

Full Changelog: [v4.59.0...v4.59.1](https://github.com/team-telnyx/telnyx-python/compare/v4.59.0...v4.59.1)

### Bug Fixes

* narrow porting event_type enums for SDK discriminator support ([7eb298c](https://github.com/team-telnyx/telnyx-python/commit/7eb298c84b686ddca5a1879d283c06616370e760))


### Chores

* **docs:** add missing descriptions ([4ceeb06](https://github.com/team-telnyx/telnyx-python/commit/4ceeb0638ea79aed95b74d8afe71ef7386f4a3af))

## 4.59.0 (2026-02-27)

Full Changelog: [v4.58.0...v4.59.0](https://github.com/team-telnyx/telnyx-python/compare/v4.58.0...v4.59.0)

### Features

* **api:** manual updates ([20c1640](https://github.com/team-telnyx/telnyx-python/commit/20c16402fd6c9c09cf4f841ce99461fb207d79de))

## 4.58.0 (2026-02-27)

Full Changelog: [v4.57.0...v4.58.0](https://github.com/team-telnyx/telnyx-python/compare/v4.57.0...v4.58.0)

### Features

* **api:** manual updates ([89bab79](https://github.com/team-telnyx/telnyx-python/commit/89bab7926861dace8848e30241c66140d65cf5ef))

## 4.57.0 (2026-02-27)

Full Changelog: [v4.56.0...v4.57.0](https://github.com/team-telnyx/telnyx-python/compare/v4.56.0...v4.57.0)

### Features

* **api:** manual updates ([6c6c4a9](https://github.com/team-telnyx/telnyx-python/commit/6c6c4a9a4641f3a60c0eddc0673657aa3a723beb))

## 4.56.0 (2026-02-27)

Full Changelog: [v4.55.0...v4.56.0](https://github.com/team-telnyx/telnyx-python/compare/v4.55.0...v4.56.0)

### Features

* Add TTS file-based endpoint spec ([718a8ad](https://github.com/team-telnyx/telnyx-python/commit/718a8ada176d2639ccff920c006473b2b222fd0d))

## 4.55.0 (2026-02-26)

Full Changelog: [v4.54.0...v4.55.0](https://github.com/team-telnyx/telnyx-python/compare/v4.54.0...v4.55.0)

### Features

* **api:** manual updates ([fdd1440](https://github.com/team-telnyx/telnyx-python/commit/fdd14403d207e6a1f0f786ef9fa0f15113ab150e))

## 4.54.0 (2026-02-26)

Full Changelog: [v4.53.0...v4.54.0](https://github.com/team-telnyx/telnyx-python/compare/v4.53.0...v4.54.0)

### Features

* **api:** manual updates ([77f1ee2](https://github.com/team-telnyx/telnyx-python/commit/77f1ee220b9f959ee907095f6be018718d5a9f54))


### Chores

* bring back other changes ([e9d29a9](https://github.com/team-telnyx/telnyx-python/commit/e9d29a9f1486fe34ec390cb7cc88f233cef79cca))

## 4.53.0 (2026-02-26)

Full Changelog: [v4.52.0...v4.53.0](https://github.com/team-telnyx/telnyx-python/compare/v4.52.0...v4.53.0)

### Features

* **api:** manual updates ([f14db77](https://github.com/team-telnyx/telnyx-python/commit/f14db77cd98183ca8919771c2ba9d01c7f9dacfc))

## 4.52.0 (2026-02-26)

Full Changelog: [v4.51.0...v4.52.0](https://github.com/team-telnyx/telnyx-python/compare/v4.51.0...v4.52.0)

### Features

* TELAPPS-ENGDESK-48951 add channels to conf record start ([6eee179](https://github.com/team-telnyx/telnyx-python/commit/6eee1798f5cdb7810d8d38dc589e75ac5c41166c))

## 4.51.0 (2026-02-26)

Full Changelog: [v4.50.0...v4.51.0](https://github.com/team-telnyx/telnyx-python/compare/v4.50.0...v4.51.0)

### Features

* **api:** manual updates ([ac454e8](https://github.com/team-telnyx/telnyx-python/commit/ac454e818dfb625a7de8363d1e54e9c795093ca9))

## 4.50.0 (2026-02-26)

Full Changelog: [v4.49.0...v4.50.0](https://github.com/team-telnyx/telnyx-python/compare/v4.49.0...v4.50.0)

### Features

* Add text-to-speech WebSocket streaming OpenAPI spec ([7c4e709](https://github.com/team-telnyx/telnyx-python/commit/7c4e7096921ae6e07ede51b783711bbdcd9c088a))

## 4.49.0 (2026-02-25)

Full Changelog: [v4.48.0...v4.49.0](https://github.com/team-telnyx/telnyx-python/compare/v4.48.0...v4.49.0)

### Features

* **api:** manual updates ([8d21974](https://github.com/team-telnyx/telnyx-python/commit/8d2197436a138d905a0961b8cdb687cb40853c64))

## 4.48.0 (2026-02-25)

Full Changelog: [v4.47.0...v4.48.0](https://github.com/team-telnyx/telnyx-python/compare/v4.47.0...v4.48.0)

### Features

* PORTAL-5923: Add stored_payment_transactions endpoint to OpenAPI docs ([b1f9469](https://github.com/team-telnyx/telnyx-python/commit/b1f94692a45fca532a50bc6711d13c3fa88e21fd))


### Documentation

* **call-control:** Add missing params to hangup, bridge, answer ([5a9edc7](https://github.com/team-telnyx/telnyx-python/commit/5a9edc7061f2792a1a0cc28bd3cb6b7a5f0f78cf))
* **call-control:** Add queue CRUD endpoints ([6495063](https://github.com/team-telnyx/telnyx-python/commit/649506339ff4257fa584f869537d2fd7febd7cad))

## 4.47.0 (2026-02-25)

Full Changelog: [v4.46.0...v4.47.0](https://github.com/team-telnyx/telnyx-python/compare/v4.46.0...v4.47.0)

### Features

* TELAPPS Add prevent_double_bridge to bridge command ([aa679f1](https://github.com/team-telnyx/telnyx-python/commit/aa679f1d214041985bd2bb3ed6c12032ef8eb688))

## 4.46.0 (2026-02-25)

Full Changelog: [v4.45.0...v4.46.0](https://github.com/team-telnyx/telnyx-python/compare/v4.45.0...v4.46.0)

### Features

* **api:** manual updates ([be08ccd](https://github.com/team-telnyx/telnyx-python/commit/be08ccd7d36d139b9307e855d2ea7f67edeb3d0a))

## 4.45.0 (2026-02-25)

Full Changelog: [v4.44.2...v4.45.0](https://github.com/team-telnyx/telnyx-python/compare/v4.44.2...v4.45.0)

### Features

* Add missing TTS voice settings schemas and update voice descriptions ([4697821](https://github.com/team-telnyx/telnyx-python/commit/4697821650151bdce373441b51ae04f9487c05eb))

## 4.44.2 (2026-02-24)

Full Changelog: [v4.44.1...v4.44.2](https://github.com/team-telnyx/telnyx-python/compare/v4.44.1...v4.44.2)

### Chores

* **internal:** make `test_proxy_environment_variables` more resilient to env ([ce75c52](https://github.com/team-telnyx/telnyx-python/commit/ce75c52b99bec75bc3fad64a7e9df9b69d62e709))

## 4.44.1 (2026-02-24)

Full Changelog: [v4.44.0...v4.44.1](https://github.com/team-telnyx/telnyx-python/compare/v4.44.0...v4.44.1)

### Chores

* **dependencies:** require standardwebhooks 1.0.1 ([f6c0916](https://github.com/team-telnyx/telnyx-python/commit/f6c09167c0eda8d914fd71fff5bded63a6f91d21))
* **internal:** add request options to SSE classes ([8c1de8c](https://github.com/team-telnyx/telnyx-python/commit/8c1de8c14fec79f7cc30e3431d44d45df5e771b2))
* **internal:** make `test_proxy_environment_variables` more resilient ([96176b0](https://github.com/team-telnyx/telnyx-python/commit/96176b0b7cc79992b1ff4cc3579944ba261d9f56))

## 4.44.0 (2026-02-22)

Full Changelog: [v4.43.4...v4.44.0](https://github.com/team-telnyx/telnyx-python/compare/v4.43.4...v4.44.0)

### Features

* **api:** manual updates ([d955c26](https://github.com/team-telnyx/telnyx-python/commit/d955c26baa879823425678b40b5b23c7d4d11c9f))

## 4.43.4 (2026-02-22)

Full Changelog: [v4.43.3...v4.43.4](https://github.com/team-telnyx/telnyx-python/compare/v4.43.3...v4.43.4)

### Bug Fixes

* OAS drift — verify.json (messaging-2fa) ([a456fe5](https://github.com/team-telnyx/telnyx-python/commit/a456fe54c14b857193bad77408bf7a48387ddc65))

## 4.43.3 (2026-02-22)

Full Changelog: [v4.43.2...v4.43.3](https://github.com/team-telnyx/telnyx-python/compare/v4.43.2...v4.43.3)

### Bug Fixes

* OAS drift — toll-free-verification.json (messaging-tf-verify) ([b87d30d](https://github.com/team-telnyx/telnyx-python/commit/b87d30d0cfbe68c9a2040e6538fe1cd61f8fd64d))

## 4.43.2 (2026-02-21)

Full Changelog: [v4.43.1...v4.43.2](https://github.com/team-telnyx/telnyx-python/compare/v4.43.1...v4.43.2)

### Bug Fixes

* OAS drift — 10dlc.json (messaging-campaign-registry) ([79965d8](https://github.com/team-telnyx/telnyx-python/commit/79965d87c6d4d49433582e88dcab684998ca4a1f))
* OAS drift — messaging.json (messaging-settings + messaging-outbound) ([d5b6964](https://github.com/team-telnyx/telnyx-python/commit/d5b69645837cb1be180e1955f2235d61b480e7cd))

## 4.43.1 (2026-02-20)

Full Changelog: [v4.43.0...v4.43.1](https://github.com/team-telnyx/telnyx-python/compare/v4.43.0...v4.43.1)

### Bug Fixes

* StringFormatNotSupported ([c4caab3](https://github.com/team-telnyx/telnyx-python/commit/c4caab3d9d25d739f2269131044d3070d10ead9f))

## 4.43.0 (2026-02-20)

Full Changelog: [v4.42.1...v4.43.0](https://github.com/team-telnyx/telnyx-python/compare/v4.42.1...v4.43.0)

### Features

* **api:** manual updates ([b30d03f](https://github.com/team-telnyx/telnyx-python/commit/b30d03fb64afaf168f72a21bfb6e586b6b06f8cc))

## 4.42.1 (2026-02-20)

Full Changelog: [v4.42.0...v4.42.1](https://github.com/team-telnyx/telnyx-python/compare/v4.42.0...v4.42.1)

### Bug Fixes

* move unsupported string formats to x-format ([7921298](https://github.com/team-telnyx/telnyx-python/commit/79212984ae4f90e7516bdaabd7fee2a220db594c))

## 4.42.0 (2026-02-20)

Full Changelog: [v4.41.0...v4.42.0](https://github.com/team-telnyx/telnyx-python/compare/v4.41.0...v4.42.0)

### Features

* fix-stainless-sdk-timeout ([632aeda](https://github.com/team-telnyx/telnyx-python/commit/632aedad6d63c5c5336133c943b5b8dbc651a078))


### Chores

* **internal:** remove mock server code ([ed56ccd](https://github.com/team-telnyx/telnyx-python/commit/ed56ccd127a9ad4eec1cd696214682ef1c6a2a95))
* update mock server docs ([e35b75f](https://github.com/team-telnyx/telnyx-python/commit/e35b75feec5cf1a0f3927eed35c344d394c59ab1))


### Documentation

* **call-control:** Add missing parameters to call control endpoints ([5dde054](https://github.com/team-telnyx/telnyx-python/commit/5dde05405daf7a3f0cf2e7f501803df6b6ae0a22))

## 4.41.0 (2026-02-19)

Full Changelog: [v4.40.0...v4.41.0](https://github.com/team-telnyx/telnyx-python/compare/v4.40.0...v4.41.0)

### Features

* **api:** manual updates ([df5af75](https://github.com/team-telnyx/telnyx-python/commit/df5af7506fb2c38686228c3a0d4058bdcbd02fd2))
* **api:** manual updates ([795c216](https://github.com/team-telnyx/telnyx-python/commit/795c216b697c41859e6d63b72dd9b24a1184e0b4))

## 4.40.0 (2026-02-19)

Full Changelog: [v4.39.0...v4.40.0](https://github.com/team-telnyx/telnyx-python/compare/v4.39.0...v4.40.0)

### Features

* **api:** manual updates ([b4361f7](https://github.com/team-telnyx/telnyx-python/commit/b4361f76fbca232c45b5d0c2a0f8beceaf257249))

## 4.39.0 (2026-02-18)

Full Changelog: [v4.38.0...v4.39.0](https://github.com/team-telnyx/telnyx-python/compare/v4.38.0...v4.39.0)

### Features

* AI-2093: Add language_boost to MiniMax voice settings ([0740caf](https://github.com/team-telnyx/telnyx-python/commit/0740caf1e59b73a32b5d8da0233631884197e43e))

## 4.38.0 (2026-02-18)

Full Changelog: [v4.37.0...v4.38.0](https://github.com/team-telnyx/telnyx-python/compare/v4.37.0...v4.38.0)

### Features

* Add smart encoding fields to messaging API spec ([5299f7e](https://github.com/team-telnyx/telnyx-python/commit/5299f7e7f251f377ac01d13f9cf38c3ee793a226))
* **api:** manual updates ([5631359](https://github.com/team-telnyx/telnyx-python/commit/5631359512011de089f40b0bfb9663c7120346f5))
* **api:** manual updates ([6a96c50](https://github.com/team-telnyx/telnyx-python/commit/6a96c5024c48fff71e424a0c07925ae143e5da5b))
* **api:** manual updates ([808c197](https://github.com/team-telnyx/telnyx-python/commit/808c1978f6c58cae8ecf219a23868e02bb607db7))

## 4.37.0 (2026-02-18)

Full Changelog: [v4.36.0...v4.37.0](https://github.com/team-telnyx/telnyx-python/compare/v4.36.0...v4.37.0)

### Features

* **api:** manual updates ([4ca1ae9](https://github.com/team-telnyx/telnyx-python/commit/4ca1ae916a1dbc07824efa0bee841ee4662f2d3f))

## 4.36.0 (2026-02-18)

Full Changelog: [v4.35.0...v4.36.0](https://github.com/team-telnyx/telnyx-python/compare/v4.35.0...v4.36.0)

### Features

* **api:** manual updates ([b6de00e](https://github.com/team-telnyx/telnyx-python/commit/b6de00e70fcaa0ef400d96cb7be733ad0f76ecc0))

## 4.35.0 (2026-02-18)

Full Changelog: [v4.34.0...v4.35.0](https://github.com/team-telnyx/telnyx-python/compare/v4.34.0...v4.35.0)

### Features

* **api:** manual updates ([2303fa3](https://github.com/team-telnyx/telnyx-python/commit/2303fa3fe9f0835d352287dc7d5bf19970b8c387))
* **api:** manual updates ([ac9e222](https://github.com/team-telnyx/telnyx-python/commit/ac9e222ccae673b9c5da38a8fe6f8142f1471c0c))

## 4.34.0 (2026-02-17)

Full Changelog: [v4.33.0...v4.34.0](https://github.com/team-telnyx/telnyx-python/compare/v4.33.0...v4.34.0)

### Features

* Align transfer tool AMD spec with portal: premium mode, drop continue actions ([088f643](https://github.com/team-telnyx/telnyx-python/commit/088f643bfacf45de13fa01c69ba4503a4bb75768))

## 4.33.0 (2026-02-17)

Full Changelog: [v4.32.0...v4.33.0](https://github.com/team-telnyx/telnyx-python/compare/v4.32.0...v4.33.0)

### Features

* Add Minimax and Resemble voice providers for speak commands ([5d87e9e](https://github.com/team-telnyx/telnyx-python/commit/5d87e9eb4868aadee770f82851d3d5f24e57633e))

## 4.32.0 (2026-02-13)

Full Changelog: [v4.31.0...v4.32.0](https://github.com/team-telnyx/telnyx-python/compare/v4.31.0...v4.32.0)

### Features

* AI-2090: Add skip_turn tool type to assistant config schema ([fc7e9ce](https://github.com/team-telnyx/telnyx-python/commit/fc7e9ced1cf790243b2fc9b191a7711ccfcc4837))

## 4.31.0 (2026-02-13)

Full Changelog: [v4.30.0...v4.31.0](https://github.com/team-telnyx/telnyx-python/compare/v4.30.0...v4.31.0)

### Features

* Add Label parameter to Dial Conference Participant endpoint ([2443fdd](https://github.com/team-telnyx/telnyx-python/commit/2443fddd6c4be617855d06e06987cc31ddcd7182))

## 4.30.0 (2026-02-13)

Full Changelog: [v4.29.0...v4.30.0](https://github.com/team-telnyx/telnyx-python/compare/v4.29.0...v4.30.0)

### Features

* ENGDESK-49554: Add quail_voice_focus to noise suppression engine enums ([1329950](https://github.com/team-telnyx/telnyx-python/commit/132995074c9ac77227f9eba75ad99a88245fcd0b))


### Chores

* format all `api.md` files ([d326b25](https://github.com/team-telnyx/telnyx-python/commit/d326b2549a4319fe68043c5be14d7e5034507134))

## 4.29.0 (2026-02-12)

Full Changelog: [v4.28.0...v4.29.0](https://github.com/team-telnyx/telnyx-python/compare/v4.28.0...v4.29.0)

### Features

* **api:** manual updates ([d7cbb74](https://github.com/team-telnyx/telnyx-python/commit/d7cbb7445e9d6e4049b45a45899ebe8e3c953188))

## 4.28.0 (2026-02-12)

Full Changelog: [v4.27.0...v4.28.0](https://github.com/team-telnyx/telnyx-python/compare/v4.27.0...v4.28.0)

### Features

* **api:** manual updates ([fc531ee](https://github.com/team-telnyx/telnyx-python/commit/fc531eebedca8ed64e41e0a3f181bdcbc2e3a710))
* **api:** manual updates to include models ([d9e935d](https://github.com/team-telnyx/telnyx-python/commit/d9e935d085028ea65ebcb5e9353c1a58bf104c98))

## 4.27.0 (2026-02-11)

Full Changelog: [v4.26.0...v4.27.0](https://github.com/team-telnyx/telnyx-python/compare/v4.26.0...v4.27.0)

### Features

* AI-2086: Add AI Missions endpoints to inference spec ([3ac4c56](https://github.com/team-telnyx/telnyx-python/commit/3ac4c569d668708c9da6467f3c4b9bd782d5ac24))


### Bug Fixes

* **client:** revert change to certain pagination metadata types ([a239d66](https://github.com/team-telnyx/telnyx-python/commit/a239d66ac555331287427686ba961556c491a9af))

## 4.26.0 (2026-02-11)

Full Changelog: [v4.25.0...v4.26.0](https://github.com/team-telnyx/telnyx-python/compare/v4.25.0...v4.26.0)

### Features

* Add OpenAI-compatible embeddings API spec ([05613d3](https://github.com/team-telnyx/telnyx-python/commit/05613d3835ff9615ac511178894e0f011dad16b6))

## 4.25.0 (2026-02-11)

Full Changelog: [v4.24.1...v4.25.0](https://github.com/team-telnyx/telnyx-python/compare/v4.24.1...v4.25.0)

### Features

* Add dynamic_variables field to scheduled event schemas ([58436b5](https://github.com/team-telnyx/telnyx-python/commit/58436b54351337dd9d54de1f0162b0ef61c6fd7b))

## 4.24.1 (2026-02-11)

Full Changelog: [v4.24.0...v4.24.1](https://github.com/team-telnyx/telnyx-python/compare/v4.24.0...v4.24.1)

### Bug Fixes

* remove invalid discriminators from string enum schemas ([b213b40](https://github.com/team-telnyx/telnyx-python/commit/b213b40e98b17c9f7dc64d0a5d4b92e8744a599b))

## 4.24.0 (2026-02-11)

Full Changelog: [v4.23.0...v4.24.0](https://github.com/team-telnyx/telnyx-python/compare/v4.23.0...v4.24.0)

### Features

* fix schema in emergency address schema ([02829b0](https://github.com/team-telnyx/telnyx-python/commit/02829b0769c07cf7fcf4ba164bd559f09c1634ea))


### Chores

* **internal:** fix lint error on Python 3.14 ([ce9c060](https://github.com/team-telnyx/telnyx-python/commit/ce9c060c2dac73429f854d73682a52888187cdc1))

## 4.23.0 (2026-02-11)

Full Changelog: [v4.22.0...v4.23.0](https://github.com/team-telnyx/telnyx-python/compare/v4.22.0...v4.23.0)

### Features

* Limit detection_mode enum to disabled and detect only ([1845ace](https://github.com/team-telnyx/telnyx-python/commit/1845ace6db0b0d7bf019dd72b86ddf8a1fc072c0))

## 4.22.0 (2026-02-09)

Full Changelog: [v4.21.0...v4.22.0](https://github.com/team-telnyx/telnyx-python/compare/v4.21.0...v4.22.0)

### Features

* AI-2078 Feature: API endpoint to disable AI assistant mid-conversation ([f9ed715](https://github.com/team-telnyx/telnyx-python/commit/f9ed715a97ba517c210de14712aca958573aedd1))

## 4.21.0 (2026-02-09)

Full Changelog: [v4.20.0...v4.21.0](https://github.com/team-telnyx/telnyx-python/compare/v4.20.0...v4.21.0)

### Features

* Revert "fix emergency settings -schema" ([ae83738](https://github.com/team-telnyx/telnyx-python/commit/ae83738d1bb520c7c070824086d9b95b82a7f69a))


### Chores

* **internal:** bump dependencies ([6700435](https://github.com/team-telnyx/telnyx-python/commit/6700435e4cd91197c7de0766e7c6082e2e505ee0))

## 4.20.0 (2026-02-05)

Full Changelog: [v4.19.0...v4.20.0](https://github.com/team-telnyx/telnyx-python/compare/v4.19.0...v4.20.0)

### Features

* **api:** Merge pull request [#23](https://github.com/team-telnyx/telnyx-python/issues/23) from stainless-sdks/fix/deepgram-nova3-enum-duplicates ([9768d83](https://github.com/team-telnyx/telnyx-python/commit/9768d838fced038745f53f8a3f90868874359127))

## 4.19.0 (2026-02-05)

Full Changelog: [v4.18.0...v4.19.0](https://github.com/team-telnyx/telnyx-python/compare/v4.18.0...v4.19.0)

### Features

* **api:** manual updates ([f206529](https://github.com/team-telnyx/telnyx-python/commit/f2065297b6cebe7bf4b917d7b8323e8f8558c35d))

## 4.18.0 (2026-02-05)

Full Changelog: [v4.17.0...v4.18.0](https://github.com/team-telnyx/telnyx-python/compare/v4.17.0...v4.18.0)

### Features

* **api:** Merge pull request [#22](https://github.com/team-telnyx/telnyx-python/issues/22) from stainless-sdks/add-all-webhook-models ([470a75f](https://github.com/team-telnyx/telnyx-python/commit/470a75fe8f9f20cbb7d4453bacab261da251d49f))

## 4.17.0 (2026-02-04)

Full Changelog: [v4.16.2...v4.17.0](https://github.com/team-telnyx/telnyx-python/compare/v4.16.2...v4.17.0)

### Features

* Add Texml parameter to create call endpoint [ENGDESK-49187] ([3db3c1c](https://github.com/team-telnyx/telnyx-python/commit/3db3c1cd082727e88ca65b20e32ed6553fc29a51))

## 4.16.2 (2026-02-02)

Full Changelog: [v4.16.1...v4.16.2](https://github.com/team-telnyx/telnyx-python/compare/v4.16.1...v4.16.2)

### Bug Fixes

* **client/oauth:** send grant_type in the right location ([1543bff](https://github.com/team-telnyx/telnyx-python/commit/1543bff8109eb8605e00d994aa627208ad608085))

## 4.16.1 (2026-01-30)

Full Changelog: [v4.16.0...v4.16.1](https://github.com/team-telnyx/telnyx-python/compare/v4.16.0...v4.16.1)

### Bug Fixes

* remove deprecated TeXML API endpoints from OpenAPI spec ([e56d9a8](https://github.com/team-telnyx/telnyx-python/commit/e56d9a84a50b4ed2e91fedb1f0fcefdaf7baf64d))
* use PaginationMeta schema for ListFaxesResponse.meta ([05e56cf](https://github.com/team-telnyx/telnyx-python/commit/05e56cf8913ffb602dac3aadfb4b4cafb610ac70))

## 4.16.0 (2026-01-29)

Full Changelog: [v4.15.0...v4.16.0](https://github.com/team-telnyx/telnyx-python/compare/v4.15.0...v4.16.0)

### Features

* **api:** revert bad update to spec ([2cecd24](https://github.com/team-telnyx/telnyx-python/commit/2cecd24094258729da3c6d2c9a65b6d22bf2acc4))

## 4.15.0 (2026-01-29)

Full Changelog: [v4.14.0...v4.15.0](https://github.com/team-telnyx/telnyx-python/compare/v4.14.0...v4.15.0)

### Features

* Add deepgram/nova-3 transcription engine option to record_start ([665efb3](https://github.com/team-telnyx/telnyx-python/commit/665efb388d75492d5468f066f3ad61e2edc8f7e0))
* **client:** add custom JSON encoder for extended type support ([bc6b681](https://github.com/team-telnyx/telnyx-python/commit/bc6b681452f280fea7c49df805f983eb16b1e957))

## 4.14.0 (2026-01-28)

Full Changelog: [v4.13.1...v4.14.0](https://github.com/team-telnyx/telnyx-python/compare/v4.13.1...v4.14.0)

### Features

* Fix broken documentation links ([dad3b13](https://github.com/team-telnyx/telnyx-python/commit/dad3b13ae93da9ec94f6e9de07d572e4c911e3f0))

## 4.13.1 (2026-01-28)

Full Changelog: [v4.13.0...v4.13.1](https://github.com/team-telnyx/telnyx-python/compare/v4.13.0...v4.13.1)

### Bug Fixes

* **docs:** fix mcp installation instructions for remote servers ([833be2a](https://github.com/team-telnyx/telnyx-python/commit/833be2a4f55f23cd36d1c9760cdcc12c7e3d6dc5))

## 4.13.0 (2026-01-28)

Full Changelog: [v4.12.0...v4.13.0](https://github.com/team-telnyx/telnyx-python/compare/v4.12.0...v4.13.0)

### Features

* Deploy dev/mc vady wip ([b023c72](https://github.com/team-telnyx/telnyx-python/commit/b023c7267115f3eefbaf5f7b5ed04f5c79c21145))

## 4.12.0 (2026-01-27)

Full Changelog: [v4.11.0...v4.12.0](https://github.com/team-telnyx/telnyx-python/compare/v4.11.0...v4.12.0)

### Features

* jira-engdesk-49089 add new connection jitter buffer related fields ([f5a8a17](https://github.com/team-telnyx/telnyx-python/commit/f5a8a17fc671831cd4d6648288c8734042fba6ba))


### Chores

* **ci:** upgrade `actions/github-script` ([f8a8baf](https://github.com/team-telnyx/telnyx-python/commit/f8a8baf0206485144e314e48a8b116d484170d13))

## 4.11.0 (2026-01-22)

Full Changelog: [v4.10.0...v4.11.0](https://github.com/team-telnyx/telnyx-python/compare/v4.10.0...v4.11.0)

### Features

* **api:** manual updates ([4522d2b](https://github.com/team-telnyx/telnyx-python/commit/4522d2b957f637e457bb31c2fadc0d83a70e5970))
* Deploy dev/mc vady wip ([23e5b7f](https://github.com/team-telnyx/telnyx-python/commit/23e5b7f49c0f6477eef4b43a6e2a93eed38a75b7))
* fix-redocly-lint-issues ([c67752d](https://github.com/team-telnyx/telnyx-python/commit/c67752d26d3002c3a01c7a0d9d9d373924cdd9b0))

## 4.10.0 (2026-01-20)

Full Changelog: [v4.9.0...v4.10.0](https://github.com/team-telnyx/telnyx-python/compare/v4.9.0...v4.10.0)

### Features

* Add Post /v2/calls/:call_control_id/actions/ai_assistant_add_messages ([cb893ca](https://github.com/team-telnyx/telnyx-python/commit/cb893ca5364798b32c17e817a11d90b73c26c48b))

## 4.9.0 (2026-01-20)

Full Changelog: [v4.8.1...v4.9.0](https://github.com/team-telnyx/telnyx-python/compare/v4.8.1...v4.9.0)

### Features

* Update voicemail_detection description with AMD enablement info ([31dee4b](https://github.com/team-telnyx/telnyx-python/commit/31dee4b086e6c800792c81e8100cef33e685864b))

## 4.8.1 (2026-01-19)

Full Changelog: [v4.8.0...v4.8.1](https://github.com/team-telnyx/telnyx-python/compare/v4.8.0...v4.8.1)

### Bug Fixes

* correct broken link to List SIM Card Actions endpoint in SIM car… ([168bb8f](https://github.com/team-telnyx/telnyx-python/commit/168bb8fd212ffb8bdef2e86d105f68705b7e450a))

## 4.8.0 (2026-01-19)

Full Changelog: [v4.7.0...v4.8.0](https://github.com/team-telnyx/telnyx-python/compare/v4.7.0...v4.8.0)

### Features

* Add AI Assistant spec updates for FE tickets ([e210abe](https://github.com/team-telnyx/telnyx-python/commit/e210abe5e60b6f55e90c08e29c3f9a110ed3063a))

## 4.7.0 (2026-01-19)

Full Changelog: [v4.6.0...v4.7.0](https://github.com/team-telnyx/telnyx-python/compare/v4.6.0...v4.7.0)

### Features

* fix-external-connection-link ([7eec114](https://github.com/team-telnyx/telnyx-python/commit/7eec1140a41b8c4e0c47c93403d406f5dc7c3324))

## 4.6.0 (2026-01-16)

Full Changelog: [v4.5.0...v4.6.0](https://github.com/team-telnyx/telnyx-python/compare/v4.5.0...v4.6.0)

### Features

* TELAPPS-5507: Add Krisp engine description for noise suppression ([f7d0db4](https://github.com/team-telnyx/telnyx-python/commit/f7d0db479b7268a01e96ac036894e9602ab92c6d))


### Bug Fixes

* update broken MDR report link in GetMessage endpoint ([e9185ec](https://github.com/team-telnyx/telnyx-python/commit/e9185ecd8b217d9330b14238b24697385e599f1d))


### Chores

* **internal:** update `actions/checkout` version ([85dbcce](https://github.com/team-telnyx/telnyx-python/commit/85dbccea6453952a190906d8693094614fdf8dd2))

## 4.5.0 (2026-01-16)

Full Changelog: [v4.4.0...v4.5.0](https://github.com/team-telnyx/telnyx-python/compare/v4.4.0...v4.5.0)

### Features

* fix links ([579f761](https://github.com/team-telnyx/telnyx-python/commit/579f76147909d1bf544b12647f587755016bc964))

## 4.4.0 (2026-01-15)

Full Changelog: [v4.3.0...v4.4.0](https://github.com/team-telnyx/telnyx-python/compare/v4.3.0...v4.4.0)

### Features

* jira-engdesk-48800 add organizations-related docs to the external api… ([9eceebd](https://github.com/team-telnyx/telnyx-python/commit/9eceebd7f791041be7960e60fcf9292d0549b581))
* MSG-6148: adding the new campaignVerifyAuthorizationToken field and missing GET OTP endpoint ([7710ded](https://github.com/team-telnyx/telnyx-python/commit/7710ded31f326d513b3d3feb7d92f9881141d88c))
* MSG-6228: MSG-6228: Add smart_encoding option for SMS character encoding optimization ([f595692](https://github.com/team-telnyx/telnyx-python/commit/f595692cc8bf5400884284ec02802998c05e914a))
* TELAPPS-ENGDESK-48790 Remove duplicated webhooks ([4e874c3](https://github.com/team-telnyx/telnyx-python/commit/4e874c34c79dd57bbe43cfffa96738a0e6040fa4))

## 4.3.0 (2026-01-14)

Full Changelog: [v4.2.0...v4.3.0](https://github.com/team-telnyx/telnyx-python/compare/v4.2.0...v4.3.0)

### Features

* **api:** fix default pagination by correctly using nested params ([ba89736](https://github.com/team-telnyx/telnyx-python/commit/ba89736a2e3293d9e50fa80932d7cbf9507bfc4f))

## 4.2.0 (2026-01-14)

Full Changelog: [v4.1.0...v4.2.0](https://github.com/team-telnyx/telnyx-python/compare/v4.1.0...v4.2.0)

### Features

* **api:** manual updates ([df8edd8](https://github.com/team-telnyx/telnyx-python/commit/df8edd8bb2b972dc4ecd7d92a679992c12536518))
* **client:** add support for binary request streaming ([91f7381](https://github.com/team-telnyx/telnyx-python/commit/91f738118fcc24c00b4e90db69441124df526b04))

## 4.1.0 (2026-01-13)

Full Changelog: [v4.0.0...v4.1.0](https://github.com/team-telnyx/telnyx-python/compare/v4.0.0...v4.1.0)

### Features

* **api:** manual updates ([f9dfa86](https://github.com/team-telnyx/telnyx-python/commit/f9dfa862cf2106360a8c2ae21164b77813d1e291))
* TELAPPS Add GET /texml/Accounts/{account_sid}/Queues endpoint ([9ab3ad6](https://github.com/team-telnyx/telnyx-python/commit/9ab3ad6a79870b258f8e1144915b3617963c7317))
* TELAPPS-ENGDESK-47967 Add black_threshold parameter to send_fax request ([0e558ed](https://github.com/team-telnyx/telnyx-python/commit/0e558ed2ecf10a49f21e3419537d6f04f0340b5c))

## 4.0.0 (2026-01-09)

Full Changelog: [v3.17.0...v4.0.0](https://github.com/team-telnyx/telnyx-python/compare/v3.17.0...v4.0.0)

### ⚠ BREAKING CHANGES

* Resolved all codegen errors

### Features

* [PORT-4538] Fix ambiguous oneOf instances on porting service and documents ([590e706](https://github.com/team-telnyx/telnyx-python/commit/590e7067ff51d2b3815ea019438eb2c38f9c72fb))
* Add AI assistant voice settings, telephony config, and tools updates ([be8d467](https://github.com/team-telnyx/telnyx-python/commit/be8d467516a1afaccfef5560439a3a6e7bfded3e))
* **api:** join all 10dlc operations into messaging_10dlc group ([c600cff](https://github.com/team-telnyx/telnyx-python/commit/c600cff7ccc52f41c695eb4241428e981d8c5744))
* **api:** manual updates ([c0aefc7](https://github.com/team-telnyx/telnyx-python/commit/c0aefc75736d4bdc6cfacdeb2e1e58146edbb72a))
* **api:** manual updates ([073b654](https://github.com/team-telnyx/telnyx-python/commit/073b65440f8c80d5c54ec64677af99a567fc738a))
* **api:** manual updates ([6821aca](https://github.com/team-telnyx/telnyx-python/commit/6821aca282284f7a2cfc2d1c4ca9113057f211fd))
* **api:** messaging_10dlc group with all their endpoints ([0ed622e](https://github.com/team-telnyx/telnyx-python/commit/0ed622e0765cc44e3f4219cf18c5d8fd81bc5184))
* **api:** reverted previous commit ([f0fdff6](https://github.com/team-telnyx/telnyx-python/commit/f0fdff6c41921c34fb9a56c70ab55240d901f000))
* Document supervising leg of call ([89c9c3d](https://github.com/team-telnyx/telnyx-python/commit/89c9c3deb8336674f4f7d585bbd2dfbb642214bb))
* DOTCOM-5179. Fix Redocly errors in outbound-voice-profiles.json ([e64e8f9](https://github.com/team-telnyx/telnyx-python/commit/e64e8f9b76b38e3c5e204dedc13193791e99f745))
* Draft. DOTCOM-5184. Fix 44 errors in the spec as reported by Redocly on video ([76c2bed](https://github.com/team-telnyx/telnyx-python/commit/76c2bedd1ef690cdb959936b5a7642240bd25b6f))
* Engdesk 47920/wireless cleanup ([8b5a65d](https://github.com/team-telnyx/telnyx-python/commit/8b5a65d81d894eed9ec78b2672a8c6618c3f5121))
* ENGDESK-47883: Fix all lint errors in telapps owned APIs ([dbdb567](https://github.com/team-telnyx/telnyx-python/commit/dbdb56771461d526c8a582aea43ab3979362c3e4))
* ENGDESK-47914 - fix warnings in numbers.json file ([ab80c9d](https://github.com/team-telnyx/telnyx-python/commit/ab80c9dd1d9ad47a5ba2776704b72d413ef85e93))
* ENGDESK-47935: Fixed unnecessary `RegionIn` schema ([46c1a8d](https://github.com/team-telnyx/telnyx-python/commit/46c1a8da131cf9b83da89d6c75110b4f768af904))
* ENGDESK-48016 - document simultaneous ringing for CredentialConnections ([52e209d](https://github.com/team-telnyx/telnyx-python/commit/52e209dc2312da39ab08f34340789433e7b7c632))
* ENGDESK-48254: Release noise suppression details docs to prod ([74341c7](https://github.com/team-telnyx/telnyx-python/commit/74341c73134986c1403914879b24c5f0fcb56f9c))
* Fix campaign usecase endpoint: /registry/enum/usecase → /10dlc/enum/usecase ([d68b8cc](https://github.com/team-telnyx/telnyx-python/commit/d68b8cc79a4eb4f2a52840a48da9d6434f67a953))
* hotfix: restore 10dlc prefixes ([21299b3](https://github.com/team-telnyx/telnyx-python/commit/21299b3b84632cbeee9195666ee43dd9c943af78))
* Improve messaging API naming and navigation ([ad2e6c6](https://github.com/team-telnyx/telnyx-python/commit/ad2e6c671cb54d88fa9e94499ff7648d1060d394))
* messaging meta object with required fields ([5cbe6fd](https://github.com/team-telnyx/telnyx-python/commit/5cbe6fde3a728db63e7394d0ae24f538316cde3e))
* Msg 6152 ([6e9ae3e](https://github.com/team-telnyx/telnyx-python/commit/6e9ae3e1a7b976396bf4dbfc7b256ace837d5fce))
* MSG-6140: Add SMS OTP endpoints for Sole Prop brands ([26f930e](https://github.com/team-telnyx/telnyx-python/commit/26f930e9d1299259efa05ed1fae198e1241b7c2d))
* MSG-6145: OTP status endpoint ([d0d0abc](https://github.com/team-telnyx/telnyx-python/commit/d0d0abcb7392ba486425415c85426098a7faa1f6))
* port-4551: remove CustomerServiceRecordStatusChanged webhook doc ([ef2ac27](https://github.com/team-telnyx/telnyx-python/commit/ef2ac27966ce401a97001ab59fb1cef923d49f35))
* PORT-4553: Add a discriminator to portout webhook ([a746e1d](https://github.com/team-telnyx/telnyx-python/commit/a746e1d887e40a5ed3bb7da448f1f79f243d8306))
* PORTAL-5787 - document query parameter to handle messaging service error ([807ac22](https://github.com/team-telnyx/telnyx-python/commit/807ac2259e91d2cccb92fa03861ba475d5e3d8af))
* TBS-3422: Fix redocly errors ([08c8ca9](https://github.com/team-telnyx/telnyx-python/commit/08c8ca90fe2ca711d605b755e480b028b35043ff))
* TELAPPS-47889 Add texml queue endpoint ([907e417](https://github.com/team-telnyx/telnyx-python/commit/907e41726ef144aab5b65d5f91fd69ef9f457d54))
* TELAPPS-5428 Add speech-to-text WS endpoint ([83c36ec](https://github.com/team-telnyx/telnyx-python/commit/83c36ec50e1a2abbb6c970c918334d3535ea582a))


### Bug Fixes

* correct broken hyperlinks in Submit Campaign endpoint description ([49f784b](https://github.com/team-telnyx/telnyx-python/commit/49f784b16b4177b44cb419f8e81c4f26511ba73c))
* make text field optional in AssistantSmsChatReq schema ([a5acf52](https://github.com/team-telnyx/telnyx-python/commit/a5acf52fce641d4ce4c5a01551ca69d63c62a177))
* **stainless:** fixes the messsages typo ([0dee0a1](https://github.com/team-telnyx/telnyx-python/commit/0dee0a119d0713a69de22fa99911e0c75e5d1021))
* use async_to_httpx_files in patch method ([eb0dd4b](https://github.com/team-telnyx/telnyx-python/commit/eb0dd4b950ed4e6e1ac987320a711b11b0813648))


### Chores

* **internal:** add `--fix` argument to lint script ([047839e](https://github.com/team-telnyx/telnyx-python/commit/047839e2958162d4136fbdd218b011634285bcf0))
* **internal:** add missing files argument to base client ([ee23a70](https://github.com/team-telnyx/telnyx-python/commit/ee23a707200a50394c3e587c59d88ab0b9c56326))
* **internal:** codegen related update ([0420502](https://github.com/team-telnyx/telnyx-python/commit/042050269eac59c78892838743b4d72845f299e5))
* Resolved all codegen errors ([017a063](https://github.com/team-telnyx/telnyx-python/commit/017a06353a9284c358fdf6fce0f62152a6f78c19))
* speedup initial import ([f805b1e](https://github.com/team-telnyx/telnyx-python/commit/f805b1e23abc2b964acb70f49f3b60c03c5864de))


### Documentation

* prominently feature MCP server setup in root SDK readmes ([5f7e635](https://github.com/team-telnyx/telnyx-python/commit/5f7e6358b1c2612157fc28f8efd865c2e071339c))

## 3.17.0 (2025-12-08)

Full Changelog: [v3.16.0...v3.17.0](https://github.com/team-telnyx/telnyx-python/compare/v3.16.0...v3.17.0)

### Features

* Chat completions response schema update ([60e2df9](https://github.com/team-telnyx/telnyx-python/commit/60e2df9ec342dceae8728c1e3332ccbb1291d105))
* ENGDESK-47706: Update TranscriptionEngineDeepgramConfig Schema ([a2e02c4](https://github.com/team-telnyx/telnyx-python/commit/a2e02c46bdfc0f1eab8cd1ec07599c12331f137e))
* ENGDESK-47886: Fix API spec for emergency.json ([da08340](https://github.com/team-telnyx/telnyx-python/commit/da083404731cd6eacf4e1fbc2244d1325957da81))
* Update default GATHER_USING_AI_MODEL ([24231bf](https://github.com/team-telnyx/telnyx-python/commit/24231bf8df309f1facc2ef9516595ac9ec22075e))


### Bug Fixes

* **api:** 10dlc prefixes ([0804bae](https://github.com/team-telnyx/telnyx-python/commit/0804baeff220e40a1587d268d169bafb166a7f4a))


### Chores

* add missing docstrings ([301071d](https://github.com/team-telnyx/telnyx-python/commit/301071ddd30601e464ce1a05b5c31235871aeada))

## 3.16.0 (2025-12-08)

Full Changelog: [v3.15.0...v3.16.0](https://github.com/team-telnyx/telnyx-python/compare/v3.15.0...v3.16.0)

### Features

* (draft/don't review) ENGDESK-38070-c: add deepgram keyword documentation ([607a743](https://github.com/team-telnyx/telnyx-python/commit/607a74391c51140cfe9cd5db754bd26010628430))
* alright, shut up redocly ([4e88b87](https://github.com/team-telnyx/telnyx-python/commit/4e88b8783bbe149f8269e48e88ceb489fa850c3a))
* ENGDESK-47736: added discriminator fields to oneOffs that were missing them ([4170527](https://github.com/team-telnyx/telnyx-python/commit/4170527d5e88f6001193cf6f0beb3e2b27a346df))
* FILE-1066: presigned url doc strings ([8a87605](https://github.com/team-telnyx/telnyx-python/commit/8a8760584e078aefa0b0b15758c408b01f603727))
* MSG-6160 fix messaging lint issues ([6f834a8](https://github.com/team-telnyx/telnyx-python/commit/6f834a85fc74de979f8058d0eb8a252c485168b0))
* MSG-6179: Add discriminator fields to Messaging API schemas for improved SDK performance ([2a6c5a9](https://github.com/team-telnyx/telnyx-python/commit/2a6c5a93a24a0d37fb393a966fd1044a87a5e1fa))
* MSG-6181: Reorganize mobile phone number messaging endpoints and fix … ([e7a118b](https://github.com/team-telnyx/telnyx-python/commit/e7a118b7ef5c468a02233638daa2da4530110b75))
* NETAPPS_687: Fixed IGW spec to match current API. ([b6fe5ec](https://github.com/team-telnyx/telnyx-python/commit/b6fe5ecc4c458a0d65cb72358557d20c74cdccfb))
* NUM-6334/NUM-6335 - fix redocly lint errors ([d61303b](https://github.com/team-telnyx/telnyx-python/commit/d61303be787360e2d7366d2375f0b930f35470c1))


### Bug Fixes

* **types:** allow pyright to infer TypedDict types within SequenceNotStr ([277b3b8](https://github.com/team-telnyx/telnyx-python/commit/277b3b8103c2be2d2ff4ec0a792fd5d5a6bce2d1))

## 3.15.0 (2025-12-03)

Full Changelog: [v3.14.0...v3.15.0](https://github.com/team-telnyx/telnyx-python/compare/v3.14.0...v3.15.0)

### Features

* **api:** manual updates ([a431d23](https://github.com/team-telnyx/telnyx-python/commit/a431d23b6049fcb07e08358b72f60ee6c34dc30a))

## 3.14.0 (2025-12-03)

Full Changelog: [v3.13.0...v3.14.0](https://github.com/team-telnyx/telnyx-python/compare/v3.13.0...v3.14.0)

### Features

* Add response schemas for telco data usage report endpoints ([fe8d5ac](https://github.com/team-telnyx/telnyx-python/commit/fe8d5ac1635793ead3ef83d5d692e048f47a4b62))
* **api:** manual updates ([61eaa6b](https://github.com/team-telnyx/telnyx-python/commit/61eaa6b5696d098266d217d1f4dba138c92edd93))
* **client:** add separate models for 2 events ([9a7b84b](https://github.com/team-telnyx/telnyx-python/commit/9a7b84b1b9be53a2e18372cb00dd1600ecee5927))
* ENGDESK-47508 - part 2 shared schema fixes ([afbdf75](https://github.com/team-telnyx/telnyx-python/commit/afbdf755540b10afbd78e9875d71796959c91a5e))
* ENGDESK-47518 document mobile number and mobile voice connection endpoints ([3d5c806](https://github.com/team-telnyx/telnyx-python/commit/3d5c80689acac891ff2bcd1212c92f8871431df1))
* ENGDESK-47580: Add quickship and exclude_held_numbers filters to inexplicit number order API ([81bdd5f](https://github.com/team-telnyx/telnyx-python/commit/81bdd5f3769f070256d4bee813545e8642c2fb2a))
* ENGDESK-47580: Add quickship and exclude_held_numbers to InexplicitNumberOrderResponse ([aff95e3](https://github.com/team-telnyx/telnyx-python/commit/aff95e3da2bde0aeacccd8d30545e2658de015e6))
* ENGDESK-47759 - fix missing meta definition in authorized ips spec ([4726a4e](https://github.com/team-telnyx/telnyx-python/commit/4726a4e6690024ab604d8805e648a928a733394f))
* Fix invalid responses ([209084d](https://github.com/team-telnyx/telnyx-python/commit/209084df5fb5f1d9a546a3018f9e23427ec350a7))
* Fixing lint errors ([852999c](https://github.com/team-telnyx/telnyx-python/commit/852999ca20da060f80143b9a3dfc3b245f577b55))
* MSG-6166 fix empty schema responses ([82dd85d](https://github.com/team-telnyx/telnyx-python/commit/82dd85de40ede239645d6de6340f206f0af4e8e8))
* PORT-4528: Fix lint errors for porting ([e8c9718](https://github.com/team-telnyx/telnyx-python/commit/e8c9718f22fdd25e98cc164f01f676cf683e36ef))
* TBS-3422: Fix TBS redocly errors ([b7e8803](https://github.com/team-telnyx/telnyx-python/commit/b7e8803b4f2762c1cb5eb654abaf214d50ea8313))


### Chores

* **docs:** use environment variables for authentication in code snippets ([b6999a6](https://github.com/team-telnyx/telnyx-python/commit/b6999a626a9940bbc4e97726e224529a78a383f5))
* update lockfile ([bf98551](https://github.com/team-telnyx/telnyx-python/commit/bf98551bcaa73daad81934ebca6b717af84d4111))

## 3.13.0 (2025-11-27)

Full Changelog: [v3.12.1...v3.13.0](https://github.com/team-telnyx/telnyx-python/compare/v3.12.1...v3.13.0)

### Features

* Ai 1967 ([8087f6d](https://github.com/team-telnyx/telnyx-python/commit/8087f6da0f0746a55d93a2b103f8f421e0178036))
* Ai 1967 part 2 ([2d809e8](https://github.com/team-telnyx/telnyx-python/commit/2d809e8dc67c19261a4eacec4d66c6571aad9712))
* Fix Redocly linting errors and warnings in TDA reporting specs ([e16e080](https://github.com/team-telnyx/telnyx-python/commit/e16e080a17161b62fbbe98a94ebceab367f068f7))
* Fix Redocly linting warnings in OAuth and Integration Secrets specs ([da507d6](https://github.com/team-telnyx/telnyx-python/commit/da507d6e268b3726694ef8b8c95e79ec1a8181bf))
* MSG-6076: webhook event for 10DLC campaign suspended status ([04d4725](https://github.com/team-telnyx/telnyx-python/commit/04d47257cf5df294a4e268317cbed1d9b9833d87))
* Refactored README to only contain useful information and reflect accu… ([ffecaa4](https://github.com/team-telnyx/telnyx-python/commit/ffecaa40fe0423f1a7636630c87275f8478b177c))
* TELAPPS-5459: Add Azure to transcription start ([c503e3e](https://github.com/team-telnyx/telnyx-python/commit/c503e3e78d7ad943e0d7863cdf4cacfeaa45767c))
* Updated README to include the step for make buildcontainer bundle to … ([4f822b8](https://github.com/team-telnyx/telnyx-python/commit/4f822b8167dfc7375eb732e28df5e7be3a7ece9c))


### Bug Fixes

* ensure streams are always closed ([ac9c87b](https://github.com/team-telnyx/telnyx-python/commit/ac9c87b9c8546a7dffb9ed4be0403cf0c1e15014))


### Chores

* **deps:** mypy 1.18.1 has a regression, pin to 1.17 ([cc2ea8e](https://github.com/team-telnyx/telnyx-python/commit/cc2ea8ea6e8d24d2e944e207192c0227039a198d))
* **internal:** codegen related update ([45049e3](https://github.com/team-telnyx/telnyx-python/commit/45049e3263e4f1b6bd332730b9753e8e4195191f))
* **internal:** codegen related update ([b4d2c6d](https://github.com/team-telnyx/telnyx-python/commit/b4d2c6d2910c9ddc9bc41afd9d829414096282a5))

## 3.12.1 (2025-11-12)

Full Changelog: [v3.12.0...v3.12.1](https://github.com/team-telnyx/telnyx-python/compare/v3.12.0...v3.12.1)

### Bug Fixes

* **compat:** update signatures of `model_dump` and `model_dump_json` for Pydantic v1 ([6ccdc25](https://github.com/team-telnyx/telnyx-python/commit/6ccdc25b1278118129d58af1acb2d5836b0721c7))

## 3.12.0 (2025-11-10)

Full Changelog: [v3.11.0...v3.12.0](https://github.com/team-telnyx/telnyx-python/compare/v3.11.0...v3.12.0)

### Features

* ENGDESK-44767 - Document force remove calls from queue ([4f3e07c](https://github.com/team-telnyx/telnyx-python/commit/4f3e07ce069af324044fe0d65f554262e55aca84))
* TELAPPS-ENGDESK-46395 Add keep_after_hangup to enqueue command ([a46975c](https://github.com/team-telnyx/telnyx-python/commit/a46975cb94df72a7abeb4b5cc25e5f3a9e8ecda6))
* TELAPPS-ENGDESK-46395 Add keep_after_hangup to enqueue command ([a66e1d6](https://github.com/team-telnyx/telnyx-python/commit/a66e1d6c8498977f92d972882e2954fecb58b5db))
* TELAPPS-ENGDESK-46395 Add PATCH /queues/{queue_name}/calls/{call_control_id} endpoint ([e68a26a](https://github.com/team-telnyx/telnyx-python/commit/e68a26acd908024e958cc1d2226c209de420e524))


### Bug Fixes

* compat with Python 3.14 ([f27f60c](https://github.com/team-telnyx/telnyx-python/commit/f27f60ced40b3636d3c17a559976a0c27e2560a8))


### Chores

* **internal/tests:** avoid race condition with implicit client cleanup ([40ec679](https://github.com/team-telnyx/telnyx-python/commit/40ec679f230637e0cd766e94a23aa37bb3936ba1))
* **internal:** codegen related update ([0c875d3](https://github.com/team-telnyx/telnyx-python/commit/0c875d3b039eb53b6c739b7b294f2f48d0dc8161))
* **internal:** codegen related update ([c1b1aed](https://github.com/team-telnyx/telnyx-python/commit/c1b1aeddfc89abb6b2a937a06d67b5e8bc2379f6))
* **internal:** codegen related update ([82c1747](https://github.com/team-telnyx/telnyx-python/commit/82c1747ec0acb375a7572c666c88f1f835711b76))
* **internal:** grammar fix (it's -&gt; its) ([6245054](https://github.com/team-telnyx/telnyx-python/commit/6245054bb0a7694a623338d331ccbc2d8c0c4668))
* **package:** drop Python 3.8 support ([322da01](https://github.com/team-telnyx/telnyx-python/commit/322da015d8137ccde0bf1f76b02247787dc9b1c1))

## 3.11.0 (2025-10-30)

Full Changelog: [v3.10.0...v3.11.0](https://github.com/team-telnyx/telnyx-python/compare/v3.10.0...v3.11.0)

### Features

* AI-1842: Add MCP Servers and Integrations sections ([8a8c1e1](https://github.com/team-telnyx/telnyx-python/commit/8a8c1e1825ab7b8261ea8ac7e035d8e3b879f41e))
* TELAPPS-5399 Add region to conference commands ([3f12db2](https://github.com/team-telnyx/telnyx-python/commit/3f12db2e89e7bcc5c6d7120db3344b0b925982af))


### Bug Fixes

* **client:** fix issue with example webhook payload ([c41b9b0](https://github.com/team-telnyx/telnyx-python/commit/c41b9b04422d0ee052b884cd295fe902d6dca2c5))


### Refactors

* **webhooks:** simplify webhook verification to function-based approach ([#7](https://github.com/team-telnyx/telnyx-python/issues/7)) ([f8ece68](https://github.com/team-telnyx/telnyx-python/commit/f8ece682653fb3169002b04e9dca970eafad7165))

## 3.10.0 (2025-10-29)

Full Changelog: [v3.9.0...v3.10.0](https://github.com/team-telnyx/telnyx-python/compare/v3.9.0...v3.10.0)

### Features

* ENGDESK-45429 - Add sip_region documentation for dial and transfer command ([59adfcd](https://github.com/team-telnyx/telnyx-python/commit/59adfcd68a21d12dc85aa969564b048fc325b384))
* ENGDESK-46399 - Add sip_call_id filter for retreiving recordings ([16958a6](https://github.com/team-telnyx/telnyx-python/commit/16958a6ed43f725e0dd8923d85c6d2740b93769f))


### Bug Fixes

* **client:** close streams without requiring full consumption ([8e32050](https://github.com/team-telnyx/telnyx-python/commit/8e320501ca64eae389e2eb33b861cec09f284eff))

## 3.9.0 (2025-10-27)

Full Changelog: [v3.8.0...v3.9.0](https://github.com/team-telnyx/telnyx-python/compare/v3.8.0...v3.9.0)

### Features

* **webhooks:** Implement custom Telnyx webhook verification ([#2](https://github.com/team-telnyx/telnyx-python/issues/2)) ([51e8440](https://github.com/team-telnyx/telnyx-python/commit/51e8440992c3b413d6c91ee5fc33578bc21c27d6))

## 3.8.0 (2025-10-21)

Full Changelog: [v3.7.0...v3.8.0](https://github.com/team-telnyx/telnyx-python/compare/v3.7.0...v3.8.0)

### Features

* **api:** added webhook public key ([1d410a8](https://github.com/team-telnyx/telnyx-python/commit/1d410a89914a1725596d96fe09bdcef1d5f48c83))

## 3.7.0 (2025-10-21)

Full Changelog: [v3.6.0...v3.7.0](https://github.com/team-telnyx/telnyx-python/compare/v3.6.0...v3.7.0)

### Features

* **api:** manual updates ([c37da89](https://github.com/team-telnyx/telnyx-python/commit/c37da89c4a58739b77408e62f61c6dd664a7fe2b))

## 3.6.0 (2025-10-21)

Full Changelog: [v3.5.0...v3.6.0](https://github.com/team-telnyx/telnyx-python/compare/v3.5.0...v3.6.0)

### Features

* **api:** add method to upload JSON documents ([c5028bb](https://github.com/team-telnyx/telnyx-python/commit/c5028bbf20b22dc10b82425eb59622361add546e))
* **api:** manual updates ([12f6545](https://github.com/team-telnyx/telnyx-python/commit/12f6545ff47c2b41f7c45cdc0de37b1c23736b4a))
* **api:** manual updates ([2250b8d](https://github.com/team-telnyx/telnyx-python/commit/2250b8d642d21b0f6629f00cfa066d6ba5eea7a8))
* define more models ([0f72fad](https://github.com/team-telnyx/telnyx-python/commit/0f72fad4e087b153f8e0fbb5bd602f1292b7d957))


### Chores

* bump `httpx-aiohttp` version to 0.1.9 ([b97919a](https://github.com/team-telnyx/telnyx-python/commit/b97919af398967c61448c7f0c328567ed13d6e23))

## 3.5.0 (2025-10-16)

Full Changelog: [v3.4.0...v3.5.0](https://github.com/team-telnyx/telnyx-python/compare/v3.4.0...v3.5.0)

### Features

* ENGDESK-45836: Document private endpoint for republishing account events ([ef2d4f5](https://github.com/team-telnyx/telnyx-python/commit/ef2d4f59b792b3653865265fa3845d1cf37ccc83))
* Fix broken link to List SIM card action ([cfb471a](https://github.com/team-telnyx/telnyx-python/commit/cfb471a27db576b59f9f592239aeb27f53168f7c))
* MSG-5978: Add BRN fields to toll-free verification OpenAPI specs ([b91e46c](https://github.com/team-telnyx/telnyx-python/commit/b91e46c9d601e74d735c1f9d4bcd8508f81ecc63))
* Retell assistants import ([99b3af8](https://github.com/team-telnyx/telnyx-python/commit/99b3af8f253027bc8e92aa282cc9ca86c6d6043e))


### Chores

* **internal:** detect missing future annotations with ruff ([d9c098b](https://github.com/team-telnyx/telnyx-python/commit/d9c098baaf9f97d6f2303ec2b482bf75f99ab4c3))

## 3.4.0 (2025-10-06)

Full Changelog: [v3.3.0...v3.4.0](https://github.com/team-telnyx/telnyx-python/compare/v3.3.0...v3.4.0)

### Features

* ENGDESK-45343: Add CustomHeaders documentation to TeXML Dial endpoints ([ee94cac](https://github.com/team-telnyx/telnyx-python/commit/ee94cacc2228a6b2c02d207e53bef535474fb196))
* MSG-5944: added mobile_only field to messaging profiles ([d34e586](https://github.com/team-telnyx/telnyx-python/commit/d34e586ab25edc4e346abf49837dfe23f5620593))

## 3.3.0 (2025-10-06)

Full Changelog: [v3.2.0...v3.3.0](https://github.com/team-telnyx/telnyx-python/compare/v3.2.0...v3.3.0)

### Features

* Fix listing deepgram languages for transcription start ([e348b76](https://github.com/team-telnyx/telnyx-python/commit/e348b7666742f3449cf70eef7801f3e68fc31026))
* TELAPPS-5367: Update transcription start docs ([ce4c62c](https://github.com/team-telnyx/telnyx-python/commit/ce4c62ca1e2c210975be6a6844efaa39244658c4))

## 3.2.0 (2025-10-01)

Full Changelog: [v3.1.0...v3.2.0](https://github.com/team-telnyx/telnyx-python/compare/v3.1.0...v3.2.0)

### Features

* **api:** manual updates ([5e05608](https://github.com/team-telnyx/telnyx-python/commit/5e05608fdb6f8d602f7df918ed09491afa4129b3))
* Engdesk 44932 ([b9b7061](https://github.com/team-telnyx/telnyx-python/commit/b9b7061707f8ed70ca643ef31fd594a020d496c3))


### Chores

* configure new SDK language ([7aa88d4](https://github.com/team-telnyx/telnyx-python/commit/7aa88d4d43461cabc3a96107b863dc4f5731f0cf))

## 3.1.0 (2025-09-30)

Full Changelog: [v3.0.0...v3.1.0](https://github.com/team-telnyx/telnyx-python/compare/v3.0.0...v3.1.0)

### ⚠ BREAKING CHANGES

* **api:** extract APIError to shared models

### Features

* AISWE-458: Remove S3 operations from OpenAPI spec ([f504203](https://github.com/team-telnyx/telnyx-python/commit/f504203bba7bf84daff33194f57b4acb8d2b0621))
* **api:** extract APIError to shared models ([8f20ea3](https://github.com/team-telnyx/telnyx-python/commit/8f20ea354d15ce66699a1b872c256920c3853eb8))
* recommend against using businessContactEmail ([8616bf4](https://github.com/team-telnyx/telnyx-python/commit/8616bf4e1c18023e575c0841ac51631c56630b7a))
* warm transfer ([9eb9c15](https://github.com/team-telnyx/telnyx-python/commit/9eb9c15000602213058fe88a705f88466439ad6f))


### Bug Fixes

* **compat:** compat with `pydantic&lt;2.8.0` when using additional fields ([f8eb065](https://github.com/team-telnyx/telnyx-python/commit/f8eb06586b920066deba23461002e6cb76ba8f83))


### Chores

* add extension variable on dev docs ([6016c06](https://github.com/team-telnyx/telnyx-python/commit/6016c06ae87381051bc85f593cde1c10fdd6d650))

## 3.0.0 (2025-09-23)

Full Changelog: [v3.7.0-alpha...v3.0.0](https://github.com/team-telnyx/telnyx-python/compare/v3.7.0-alpha...v3.0.0)

### Chores

* trigger CI/CD pipeline ([e2a1c9d](https://github.com/team-telnyx/telnyx-python/commit/e2a1c9d5f7d6e0c64ed3e7b3578aff0684283f47))

## 3.7.0-alpha (2025-09-23)

Full Changelog: [v3.6.0-alpha...v3.7.0-alpha](https://github.com/team-telnyx/telnyx-python/compare/v3.6.0-alpha...v3.7.0-alpha)

### Features

* **api:** manual updates ([aee8355](https://github.com/team-telnyx/telnyx-python/commit/aee8355d4c368124161e2ac0f8c7f9ab87010b0e))

## 3.6.0-alpha (2025-09-23)

Full Changelog: [v3.5.0-alpha...v3.6.0-alpha](https://github.com/team-telnyx/telnyx-python/compare/v3.5.0-alpha...v3.6.0-alpha)

### Features

* **api:** manual updates ([12d91f6](https://github.com/team-telnyx/telnyx-python/commit/12d91f63949e7097d424fabd0de50fa74f7cce65))
* **api:** manual updates ([04e377e](https://github.com/team-telnyx/telnyx-python/commit/04e377ec69cfdfadb46eff9f4008dee6460ec21a))


### Chores

* do not install brew dependencies in ./scripts/bootstrap by default ([f6d0905](https://github.com/team-telnyx/telnyx-python/commit/f6d09059d41e721669697646dc072b9eca5e2c5b))
* improve example values ([38fccc3](https://github.com/team-telnyx/telnyx-python/commit/38fccc3883c842b436400beab2f5cc9932bc9039))

## 3.5.0-alpha (2025-09-19)

Full Changelog: [v3.4.0-alpha...v3.5.0-alpha](https://github.com/team-telnyx/telnyx-python/compare/v3.4.0-alpha...v3.5.0-alpha)

### Features

* **api:** manual updates ([d4fd511](https://github.com/team-telnyx/telnyx-python/commit/d4fd5118081b91c12d3bf2a77c0ba1f12a7a04cb))
* **api:** manual updates ([0eb047b](https://github.com/team-telnyx/telnyx-python/commit/0eb047bc54d338569aa15df91c1ebf7f741f3ec8))
* **api:** rename enums with problematic characters ([1334c75](https://github.com/team-telnyx/telnyx-python/commit/1334c755da81fe115f35af23fceb1064fd3c2bc5))


### Chores

* **internal:** update pydantic dependency ([09a43dc](https://github.com/team-telnyx/telnyx-python/commit/09a43dc632831b1d7ae2f571a8d426cb57422526))
* **types:** change optional parameter type from NotGiven to Omit ([6d7998b](https://github.com/team-telnyx/telnyx-python/commit/6d7998be4ca9225e05ce8e17a7cd92b3ba5aeb06))

## 3.4.0-alpha (2025-09-09)

Full Changelog: [v3.3.0-alpha...v3.4.0-alpha](https://github.com/team-telnyx/telnyx-python/compare/v3.3.0-alpha...v3.4.0-alpha)

### Features

* improve future compat with pydantic v3 ([73c0860](https://github.com/team-telnyx/telnyx-python/commit/73c086030a85645d66a8c743c7fe26e35f25b835))
* **types:** replace List[str] with SequenceNotStr in params ([e59f69c](https://github.com/team-telnyx/telnyx-python/commit/e59f69c554f2a6e08323d1622bc60cba509c0e29))


### Chores

* **internal:** add Sequence related utils ([7b67814](https://github.com/team-telnyx/telnyx-python/commit/7b678144f51fa389e0277ce3f9ac3bbc5593636c))
* **internal:** codegen related update ([e0b95dc](https://github.com/team-telnyx/telnyx-python/commit/e0b95dcd80a265ca31597a597d344bd97a07be28))
* **internal:** move mypy configurations to `pyproject.toml` file ([3e006df](https://github.com/team-telnyx/telnyx-python/commit/3e006df10471a1e4730b03eca1c9399e744c659f))

## 3.3.0-alpha (2025-08-27)

Full Changelog: [v3.2.0-alpha...v3.3.0-alpha](https://github.com/team-telnyx/telnyx-python/compare/v3.2.0-alpha...v3.3.0-alpha)

### Features

* **api:** manual updates ([c471f6f](https://github.com/team-telnyx/telnyx-python/commit/c471f6f7595e375725124181460385b57c3335f4))

## 3.2.0-alpha (2025-08-27)

Full Changelog: [v3.1.0-alpha...v3.2.0-alpha](https://github.com/team-telnyx/telnyx-python/compare/v3.1.0-alpha...v3.2.0-alpha)

### Features

* port-4304: add public download document link specs ([c99efa8](https://github.com/team-telnyx/telnyx-python/commit/c99efa8fe272848ccdb18b984238b44f065dd0b2))

## 3.1.0-alpha (2025-08-27)

Full Changelog: [v3.0.0-alpha...v3.1.0-alpha](https://github.com/team-telnyx/telnyx-python/compare/v3.0.0-alpha...v3.1.0-alpha)

### Features

* AISWE-429: Upgrade call-control call-control OpenAPI to 3.1 with Standard Webhooks ([c6498e6](https://github.com/team-telnyx/telnyx-python/commit/c6498e6e628c19175191de0092ba897c69318d0d))
* AISWE-429: Upgrade messaging 10dlc OpenAPI to 3.1 with Standard Webhooks ([e0cf35f](https://github.com/team-telnyx/telnyx-python/commit/e0cf35f4d12d8f24e26dab02909e238c02d22465))
* AISWE-429: Upgrade messaging messaging OpenAPI to 3.1 with Standard Webhooks ([c005985](https://github.com/team-telnyx/telnyx-python/commit/c005985aaacf9a41cf889bf15e6eb40d1a773e44))
* AISWE-429: Upgrade numbers numbers OpenAPI to 3.1 with Standard Webhooks ([9448fc5](https://github.com/team-telnyx/telnyx-python/commit/9448fc586b6de3896cfacc01f4153650c3cd0d2b))
* AISWE-429: Upgrade porting customer_service_record OpenAPI to 3.1 with Standard Webhooks ([ea07f5c](https://github.com/team-telnyx/telnyx-python/commit/ea07f5c8688b990d4890f28e377ec20074993ace))
* AISWE-429: Upgrade programmable-fax programmable-fax OpenAPI to 3.1 with Standard Webhooks ([0ce7e38](https://github.com/team-telnyx/telnyx-python/commit/0ce7e38f1a87f45e1a60570322bae101b8646286))
* **api:** rename Error to MessagesError ([ac58be4](https://github.com/team-telnyx/telnyx-python/commit/ac58be4181157fce47ac0bbc077dc2f0b73985e8))
* NUM-6108: Update Advanced Order API reference to include requirement_groups ([d0cc66f](https://github.com/team-telnyx/telnyx-python/commit/d0cc66f4a4faa41a557cf3b27d30f465f724dcd4))
* port-4315: add country_code filter to description ([7f7b678](https://github.com/team-telnyx/telnyx-python/commit/7f7b678b435cab29addaaff865275d9d0f0ffed7))
* port-4315: add filter by country code ([920c561](https://github.com/team-telnyx/telnyx-python/commit/920c561527177a01119fb4c542227d2cfff02998))


### Bug Fixes

* avoid newer type syntax ([1f4d346](https://github.com/team-telnyx/telnyx-python/commit/1f4d346115cbe1f985e9f711716d47c891487440))


### Chores

* **internal:** change ci workflow machines ([c87408f](https://github.com/team-telnyx/telnyx-python/commit/c87408f180f76257a61fcbfc173d3ddc1890be8d))
* **internal:** update pyright exclude list ([4863f67](https://github.com/team-telnyx/telnyx-python/commit/4863f67905e609ceb919323d86802c69bad660f8))
* update github action ([f445c07](https://github.com/team-telnyx/telnyx-python/commit/f445c07c8a4e60a8c61b24925f0545b0bdd8f074))

## 3.0.0-alpha (2025-08-18)

Full Changelog: [v0.0.1...v3.0.0-alpha](https://github.com/team-telnyx/telnyx-python/compare/v0.0.1...v3.0.0-alpha)

### Features

* add black to dev dependencies in setup.py ([563786f](https://github.com/team-telnyx/telnyx-python/commit/563786f7193a0d79d8275311d5f56034a7fc08c4))
* **api:** manual updates ([ca87ea8](https://github.com/team-telnyx/telnyx-python/commit/ca87ea8e651e6cc9ba59cfda314426fbbc972a30))
* **api:** manual updates ([471c6c1](https://github.com/team-telnyx/telnyx-python/commit/471c6c120cf12221bc29782f4ebbdacf651873da))
* MSG-5699: rcs_agents paths should be prefixed by /messaging/rcs ([f8c8915](https://github.com/team-telnyx/telnyx-python/commit/f8c8915795a49c1e81cfdd239df6c76311228376))


### Bug Fixes

* Fix Recording API endpoint and class name to match Telnyx API ([#92](https://github.com/team-telnyx/telnyx-python/issues/92)) ([9645f97](https://github.com/team-telnyx/telnyx-python/commit/9645f979af89e58c59e59a45d8f05ce87b597956))
* Make nested_id optional for PUT operations and use put_ prefix for method names ([#89](https://github.com/team-telnyx/telnyx-python/issues/89)) ([64e1c23](https://github.com/team-telnyx/telnyx-python/commit/64e1c2397e98d6a957c9c0bcdd0423c9052c7067))
* move 'black' from extras_require to install_requires in setup.py ([83efcfc](https://github.com/team-telnyx/telnyx-python/commit/83efcfc5510fb6e210adbb270f05c68ee991e1e2))


### Chores

* **docs:** Created comparison and migration doc ([b2104cf](https://github.com/team-telnyx/telnyx-python/commit/b2104cfcdb627fd7880dec5f748988c6c7f04817))
* **docs:** fixed text wrapping under Resource Access Pattern ([3349055](https://github.com/team-telnyx/telnyx-python/commit/3349055aca80d1d5cbdf34e5009f1ac77cd24e31))
* sync repo ([0fd85db](https://github.com/team-telnyx/telnyx-python/commit/0fd85db8308098a0f3913d92a92a727fea959e66))
* update SDK settings ([e5f0ac2](https://github.com/team-telnyx/telnyx-python/commit/e5f0ac29ffef95c5e60e9130c62d65f76f620673))


### Build System

* update black dependency to version 23.0 or higher in setup.py ([361c041](https://github.com/team-telnyx/telnyx-python/commit/361c041e49a0d573a8657768cb7b1a7f3fe9fdd7))
