-- public.categories definition

-- Drop table

-- DROP TABLE public.categories;

CREATE TABLE public.categories (
	category_id serial4 NOT NULL,
	category_name varchar(100) NULL,
	is_deleted bool NULL,
	created_by varchar(255) NULL,
	created_time timestamp NULL,
	modified_by varchar(255) NULL,
	modified_time timestamp NULL,
	CONSTRAINT pk_categories PRIMARY KEY (category_id)
);
CREATE UNIQUE INDEX categories_pk ON public.categories USING btree (category_id);


-- public.how_to_cooks definition

-- Drop table

-- DROP TABLE public.how_to_cooks;

CREATE TABLE public.how_to_cooks (
	how_to_cook_id int8 NOT NULL,
	description varchar(255) NULL,
	"position" int4 NULL,
	CONSTRAINT how_to_cooks_pkey PRIMARY KEY (how_to_cook_id)
);


-- public.ingridients definition

-- Drop table

-- DROP TABLE public.ingridients;

CREATE TABLE public.ingridients (
	ingridient_id int8 NOT NULL,
	ingridient_measurement varchar(255) NULL,
	ingridient_name varchar(255) NULL,
	ingridient_quantity int4 NULL,
	CONSTRAINT ingridients_pkey PRIMARY KEY (ingridient_id)
);


-- public.levels definition

-- Drop table

-- DROP TABLE public.levels;

CREATE TABLE public.levels (
	level_id serial4 NOT NULL,
	level_name varchar(100) NULL,
	is_deleted bool NULL,
	created_by varchar(255) NULL,
	created_time timestamp NULL,
	modified_by varchar(255) NULL,
	modified_time timestamp NULL,
	CONSTRAINT pk_levels PRIMARY KEY (level_id)
);
CREATE UNIQUE INDEX levels_pk ON public.levels USING btree (level_id);


-- public.roles definition

-- Drop table

-- DROP TABLE public.roles;

CREATE TABLE public.roles (
	role_id int8 NOT NULL,
	role_name varchar(255) NULL,
	CONSTRAINT roles_pkey PRIMARY KEY (role_id)
);


-- public.users definition

-- Drop table

-- DROP TABLE public.users;

CREATE TABLE public.users (
	user_id serial4 NOT NULL,
	username varchar(255) NULL,
	fullname varchar(255) NULL,
	"password" text NULL,
	"role" varchar(100) NULL,
	is_deleted bool NULL,
	created_by varchar(255) NULL,
	created_time timestamp NULL,
	modified_by varchar(255) NULL,
	modified_time timestamp NULL,
	role_id int8 NULL,
	CONSTRAINT ckc_role_users CHECK (((role IS NULL) OR ((role)::text = ANY ((ARRAY['Admin'::character varying, 'User'::character varying])::text[])))),
	CONSTRAINT pk_users PRIMARY KEY (user_id),
	CONSTRAINT fkp56c1712k691lhsyewcssf40f FOREIGN KEY (role_id) REFERENCES public.roles(role_id)
);
CREATE UNIQUE INDEX users_pk ON public.users USING btree (user_id);


-- public.recipes definition

-- Drop table

-- DROP TABLE public.recipes;

CREATE TABLE public.recipes (
	recipe_id serial4 NOT NULL,
	user_id int4 NULL,
	category_id int4 NULL,
	level_id int4 NULL,
	recipe_name varchar(255) NULL,
	image_filename text NULL,
	time_cook int4 NULL,
	ingredient text NULL,
	how_to_cook text NULL,
	is_deleted bool NULL,
	created_by varchar(255) NULL,
	created_time timestamp NULL,
	modified_by varchar(255) NULL,
	modified_time timestamp NULL,
	image_url varchar(255) NULL,
	"time" int4 NULL,
	CONSTRAINT pk_recipes PRIMARY KEY (recipe_id),
	CONSTRAINT fk_recipes_relations_categori FOREIGN KEY (category_id) REFERENCES public.categories(category_id) ON DELETE RESTRICT ON UPDATE RESTRICT,
	CONSTRAINT fk_recipes_relations_levels FOREIGN KEY (level_id) REFERENCES public.levels(level_id) ON DELETE RESTRICT ON UPDATE RESTRICT,
	CONSTRAINT fk_recipes_relations_users FOREIGN KEY (user_id) REFERENCES public.users(user_id) ON DELETE RESTRICT ON UPDATE RESTRICT
);
CREATE UNIQUE INDEX recipes_pk ON public.recipes USING btree (recipe_id);
CREATE INDEX relationship_2_fk ON public.recipes USING btree (category_id);
CREATE INDEX relationship_3_fk ON public.recipes USING btree (level_id);
CREATE INDEX relationship_5_fk ON public.recipes USING btree (user_id);


-- public.favorite_foods definition

-- Drop table

-- DROP TABLE public.favorite_foods;

CREATE TABLE public.favorite_foods (
	user_id int4 NULL,
	recipe_id int4 NULL,
	is_favorite bool NULL,
	created_by varchar(255) NULL,
	created_time timestamp NULL,
	modified_by varchar(255) NULL,
	modified_time timestamp NULL,
	CONSTRAINT fk_favorite_relations_recipes FOREIGN KEY (recipe_id) REFERENCES public.recipes(recipe_id) ON DELETE RESTRICT ON UPDATE RESTRICT,
	CONSTRAINT fk_favorite_relations_users FOREIGN KEY (user_id) REFERENCES public.users(user_id) ON DELETE RESTRICT ON UPDATE RESTRICT
);
CREATE INDEX relationship_1_fk ON public.favorite_foods USING btree (recipe_id);
CREATE INDEX relationship_4_fk ON public.favorite_foods USING btree (user_id);


-- public.recipe_how_to_cook definition

-- Drop table

-- DROP TABLE public.recipe_how_to_cook;

CREATE TABLE public.recipe_how_to_cook (
	how_to_cook_id int8 NOT NULL,
	recipe_id int8 NOT NULL,
	CONSTRAINT recipe_how_to_cook_pkey PRIMARY KEY (how_to_cook_id, recipe_id),
	CONSTRAINT fkci3xmv15binu430vnuv4d3dg5 FOREIGN KEY (how_to_cook_id) REFERENCES public.how_to_cooks(how_to_cook_id),
	CONSTRAINT fkl6au6vcjd2r8wkfsjlsw0uvmq FOREIGN KEY (recipe_id) REFERENCES public.recipes(recipe_id)
);


-- public.recipe_ingridient definition

-- Drop table

-- DROP TABLE public.recipe_ingridient;

CREATE TABLE public.recipe_ingridient (
	ingridient_id int8 NOT NULL,
	recipe_id int8 NOT NULL,
	CONSTRAINT recipe_ingridient_pkey PRIMARY KEY (ingridient_id, recipe_id),
	CONSTRAINT fk5vdiinq2fdnn74qh3ua35il0x FOREIGN KEY (ingridient_id) REFERENCES public.ingridients(ingridient_id),
	CONSTRAINT fkfy44cyo44ed3tprpbg21pttky FOREIGN KEY (recipe_id) REFERENCES public.recipes(recipe_id)
);