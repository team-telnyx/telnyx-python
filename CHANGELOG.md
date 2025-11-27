# Changelog

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
