# Changelog

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
