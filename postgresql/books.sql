--
-- PostgreSQL database dump
--

-- Dumped from database version 13.1
-- Dumped by pg_dump version 13.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: authors; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.authors (
    id integer,
    surname text,
    given_name text,
    birth_year integer,
    death_year integer
);


--
-- Name: books; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.books (
    id integer,
    title text,
    publication_year integer
);


--
-- Name: books_authors; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.books_authors (
    book_id integer,
    author_id integer
);


--
-- Data for Name: authors; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.authors (id, surname, given_name, birth_year, death_year) FROM stdin;
0	Willis	Connie	1945	\N
1	Christie	Agatha	1890	1976
2	Morrison	Toni	1931	\N
4	Austen	Jane	1775	1817
5	Gaiman	Neil	1960	\N
6	Pratchett	Terry	1948	2015
7	Brontë	Charlotte	1816	1855
8	Wodehouse	Pelham Grenville	1881	1975
9	García Márquez	Gabriel	1927	2014
10	Lewis	Sinclair	1885	1951
11	Rushdie	Salman	1947	\N
12	Bujold	Lois McMaster	1949	\N
13	Melville	Herman	1819	1891
14	Brontë	Ann	1820	1849
15	Brontë	Emily	1818	1848
16	Sterne	Laurence	1713	1768
\.


--
-- Data for Name: books; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.books (id, title, publication_year) FROM stdin;
0	All Clear	2010
1	And Then There Were None	1939
2	Beloved	1987
3	Blackout	2010
4	Elmer Gantry	1927
5	Emma	1815
6	Good Omens	1990
7	Jane Eyre	1847
8	Leave it to Psmith	1923
9	Love in the Time of Cholera	1985
10	Main Street	1920
11	Midnight's Children	1981
12	Mirror Dance	1994
13	Moby Dick	1851
14	Murder on the Orient Express	1934
15	Neverwhere	1996
16	Omoo	1847
17	One Hundred Years of Solitude	1967
18	Pride and Prejudice	1813
19	Right Ho, Jeeves	1934
20	Sense and Sensibility	1813
21	Shards of Honor	1986
22	Sula	1973
23	The Code of the Woosters	1938
24	The Satanic Verses	1988
25	The Tenant of Wildfell Hall	1848
26	Thief of Time	1996
27	To Say Nothing of the Dog	1997
28	Villette	1853
29	Wuthering Heights	1847
30	The Life and Opinions of Tristram Shandy, Gentleman	1759
\.


--
-- Data for Name: books_authors; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.books_authors (book_id, author_id) FROM stdin;
0	0
1	1
2	2
3	0
4	10
5	4
6	5
6	6
7	7
8	8
9	9
10	10
11	11
12	12
13	13
14	1
15	5
16	13
17	9
18	4
19	8
20	4
21	12
22	2
23	8
24	11
25	14
26	6
27	0
28	7
29	15
30	16
\.


--
-- PostgreSQL database dump complete
--

