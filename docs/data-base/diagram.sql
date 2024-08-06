CREATE TABLE "fields_values"(
    "id" BIGINT NOT NULL,
    "id_fields" BIGINT NOT NULL,
    "value" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "fields_values" ADD PRIMARY KEY("id");
CREATE TABLE "preferences"(
    "id" BIGINT NOT NULL,
    "id_users" BIGINT NOT NULL,
    "id_category" BIGINT NOT NULL,
    "rating" DECIMAL(8, 2) NOT NULL,
    "options" VARCHAR(4096) NOT NULL
);
ALTER TABLE
    "preferences" ADD PRIMARY KEY("id");
CREATE TABLE "category_fields"(
    "id_category" BIGINT NOT NULL,
    "id_fields" BIGINT NOT NULL
);
CREATE TABLE "fields"(
    "id" BIGINT NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "units" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "fields" ADD PRIMARY KEY("id");
CREATE TABLE "category"(
    "id" BIGINT NOT NULL,
    "name" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "category" ADD PRIMARY KEY("id");
CREATE TABLE "users"(
    "id" BIGINT NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "password" VARCHAR(255) NOT NULL,
    "email" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "users" ADD PRIMARY KEY("id");
ALTER TABLE
    "users" ADD CONSTRAINT "users_email_unique" UNIQUE("email");
ALTER TABLE
    "category_fields" ADD CONSTRAINT "category_fields_id_category_foreign" FOREIGN KEY("id_category") REFERENCES "category"("id");
ALTER TABLE
    "fields_values" ADD CONSTRAINT "fields_values_id_fields_foreign" FOREIGN KEY("id_fields") REFERENCES "fields"("id");
ALTER TABLE
    "preferences" ADD CONSTRAINT "preferences_id_users_foreign" FOREIGN KEY("id_users") REFERENCES "users"("id");
ALTER TABLE
    "preferences" ADD CONSTRAINT "preferences_id_category_foreign" FOREIGN KEY("id_category") REFERENCES "category"("id");
ALTER TABLE
    "category_fields" ADD CONSTRAINT "category_fields_id_fields_foreign" FOREIGN KEY("id_fields") REFERENCES "fields"("id");