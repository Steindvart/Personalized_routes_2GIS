CREATE TABLE "categories"(
    "id" BIGINT NOT NULL,
    "name" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "categories" ADD PRIMARY KEY("id");
CREATE TABLE "categories_fields"(
    "category_id" BIGINT NOT NULL,
    "field_id" BIGINT NOT NULL
);
CREATE TABLE "fields_values"(
    "id" BIGINT NOT NULL,
    "field_id" BIGINT NOT NULL,
    "value" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "fields_values" ADD PRIMARY KEY("id");
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
CREATE TABLE "fields"(
    "id" BIGINT NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "units" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "fields" ADD PRIMARY KEY("id");
CREATE TABLE "preferences"(
    "id" BIGINT NOT NULL,
    "user_id" BIGINT NOT NULL,
    "category_id" BIGINT NOT NULL,
    "rating" DECIMAL(8, 2) NOT NULL,
    "options" VARCHAR(4096) NOT NULL
);
ALTER TABLE
    "preferences" ADD PRIMARY KEY("id");
ALTER TABLE
    "categories_fields" ADD CONSTRAINT "categories_fields_field_id_foreign" FOREIGN KEY("field_id") REFERENCES "fields"("id");
ALTER TABLE
    "preferences" ADD CONSTRAINT "preferences_category_id_foreign" FOREIGN KEY("category_id") REFERENCES "categories"("id");
ALTER TABLE
    "fields_values" ADD CONSTRAINT "fields_values_field_id_foreign" FOREIGN KEY("field_id") REFERENCES "fields"("id");
ALTER TABLE
    "preferences" ADD CONSTRAINT "preferences_user_id_foreign" FOREIGN KEY("user_id") REFERENCES "users"("id");
ALTER TABLE
    "categories_fields" ADD CONSTRAINT "categories_fields_category_id_foreign" FOREIGN KEY("category_id") REFERENCES "categories"("id");