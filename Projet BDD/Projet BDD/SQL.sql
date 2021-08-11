-- Table: public.constucteur

-- DROP TABLE public.constucteur;

CREATE TABLE public.constucteur
(
    nom_cons character varying COLLATE pg_catalog."default" NOT NULL,
    d_f_cons character varying COLLATE pg_catalog."default",
    adr_cons character varying COLLATE pg_catalog."default",
    CONSTRAINT constucteur_pkey PRIMARY KEY (nom_cons)
)

TABLESPACE pg_default;

ALTER TABLE public.constucteur
    OWNER to postgres;

-- Table: public.pays

-- DROP TABLE public.pays;

CREATE TABLE public.pays
(
    nom_pays character varying COLLATE pg_catalog."default" NOT NULL,
    hbt_pays integer,
    cpt_pays character varying COLLATE pg_catalog."default",
    CONSTRAINT pays_pkey PRIMARY KEY (nom_pays)
)

TABLESPACE pg_default;

ALTER TABLE public.pays
    OWNER to postgres;

    -- Table: public.compagnie

    -- DROP TABLE public.compagnie;

CREATE TABLE public.compagnie
(
    num_comp character varying COLLATE pg_catalog."default" NOT NULL,
    nom_comp character varying COLLATE pg_catalog."default",
    creat_comp character varying COLLATE pg_catalog."default",
    nom_pays character varying COLLATE pg_catalog."default",
    CONSTRAINT compagnie_pkey PRIMARY KEY (num_comp),
    CONSTRAINT compagnie_nom_pays_fkey FOREIGN KEY (nom_pays)
        REFERENCES public.pays (nom_pays) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE public.compagnie
    OWNER to postgres;
-- Table: public.avion

-- DROP TABLE public.avion;

CREATE TABLE public.avion
(
    id_avion character varying COLLATE pg_catalog."default" NOT NULL,
    hr_vol integer,
    d_p_vol character varying COLLATE pg_catalog."default",
    nom_cons character varying COLLATE pg_catalog."default",
    CONSTRAINT "Avion_pkey" PRIMARY KEY (id_avion),
    CONSTRAINT avion_nom_cons_fkey FOREIGN KEY (nom_cons)
        REFERENCES public.constucteur (nom_cons) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE public.avion
    OWNER to postgres;

-- Table: public.personnel

-- DROP TABLE public.personnel;

CREATE TABLE public.personnel
(
    num_pers character varying COLLATE pg_catalog."default" NOT NULL,
    nom_pers character varying COLLATE pg_catalog."default",
    "pré_pers" character varying COLLATE pg_catalog."default",
    qual_pers character varying COLLATE pg_catalog."default",
    num_comp character varying COLLATE pg_catalog."default",
    CONSTRAINT personnel_pkey PRIMARY KEY (num_pers),
    CONSTRAINT personnel_num_comp_fkey FOREIGN KEY (num_comp)
        REFERENCES public.compagnie (num_comp) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE public.personnel
    OWNER to postgres;
