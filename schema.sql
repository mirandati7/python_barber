
CREATE TABLE public.barbearia (
    id serial NOT NULL PRIMARY KEY,
    nome character varying(60),
    telefone character varying(15),
    endereco character varying(250),
    forma_pagamento character varying(250)
);

CREATE TABLE public.cliente (
    id serial NOT NULL PRIMARY KEY,
    sexo character varying(1),
    nome character varying(100),
    telefone character varying(15),
    senha character varying(60),
    observacao character varying(500)
);


CREATE TABLE public.profissionais (
    id serial NOT NULL PRIMARY KEY,
    nome character varying(100),
    telefone character varying(15),
    senha character varying(60)
);


CREATE TABLE public.profissionais_servicos (
    id serial NOT NULL PRIMARY KEY,
    id_profissional integer,
    id_servico integer
);

CREATE TABLE public.servico (
    id serial NOT NULL PRIMARY KEY,
    nome character varying(60),
    tempo_estimado time without time zone,
    valor_servico numeric(9,2)
);


CREATE TABLE public.agendamento (
    id serial NOT NULL PRIMARY KEY,
    id_cliente integer,
    id_profissional integer,
    id_servico integer,
    data_hora timestamp without time zone,
    valor_servico numeric(9,2),
    status integer
);



ALTER TABLE ONLY public.agendamento
    ADD CONSTRAINT agendamento_id_cliente_fkey FOREIGN KEY (id_cliente) REFERENCES public.cliente(id);


ALTER TABLE ONLY public.agendamento
    ADD CONSTRAINT agendamento_id_profissional_fkey FOREIGN KEY (id_profissional) REFERENCES public.profissionais(id);


ALTER TABLE ONLY public.agendamento
    ADD CONSTRAINT agendamento_id_servico_fkey FOREIGN KEY (id_servico) REFERENCES public.servico(id);


ALTER TABLE ONLY public.profissionais_servicos
    ADD CONSTRAINT profissionais_servicos_id_profissional_fkey FOREIGN KEY (id_profissional) REFERENCES public.profissionais(id);

ALTER TABLE ONLY public.profissionais_servicos
    ADD CONSTRAINT profissionais_servicos_id_servico_fkey FOREIGN KEY (id_servico) REFERENCES public.servico(id);

