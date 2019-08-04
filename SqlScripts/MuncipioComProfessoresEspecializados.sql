
--Exibe a porcentagem das Cidades que possuem escolas com professores com especialização 

DECLARE @CidadeEscola TABLE
(
	Cidade VARCHAR(500),
	QuantidadeEscola INT
)

DECLARE @CidadeEspecializada TABLE
(
	Cidade VARCHAR(500),
	QuantidadeEscolaEspecializada INT
)


INSERT INTO @CidadeEscola
SELECT Cidade, 
	   count(Escola) AS QuantidadeEscola
FROM PerfilRespondentes
WHERE SegmentoRespondente = 'Professores' 
group by Cidade


INSERT INTO @CidadeEspecializada
SELECT p.Cidade, 
	   count(p.Escola) AS QuantidadeEscolaEspecializada 
FROM PerfilRespondentes p 
WHERE p.SegmentoRespondente = 'Professores' 
and p.Questao in('Pós-Graduação') 
group by p.Cidade


select CidadeEscola.Cidade, 
		CidadeEscola.QuantidadeEscola, 
		CidadeEspecializada.QuantidadeEscolaEspecializada,
		ROUND(((CidadeEspecializada.QuantidadeEscolaEspecializada * 100) / CidadeEscola.QuantidadeEscola),2) as Porcentagem
from @CidadeEscola CidadeEscola 
inner join @CidadeEspecializada CidadeEspecializada on CidadeEscola.Cidade = CidadeEspecializada.Cidade
order by CidadeEscola.Cidade

