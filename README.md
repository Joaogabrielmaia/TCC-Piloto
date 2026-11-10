# TCC — Erros de condição de fronteira em código Python gerado por LLMs

Pacote de replicação do piloto ampliado (TCC I, PUC Minas, Engenharia de Software).
Autores: João Gabriel Maia da Costa e Lucas Alves Resende.
Orientadores: Leonardo Vilela Cardoso e Glender Brás de Medeiros.

## Amostra
- `data/triagem-final.csv`: decisão de elegibilidade das 163 tarefas candidatas
  (triagem manual e independente dos dois autores, kappa = 0,49, divergências resolvidas por consenso).
- `data/amostra-30-tarefas.csv`: 15 tarefas do HumanEval+ e 15 do MBPP+, sorteadas com semente 20261109.
- `testes_fronteira.py`: testes de fronteira (limite e vizinhos), com o trecho do enunciado que justifica cada oráculo.

## Ordem de execução (Python 3.13, pytest 9.2, pytest-randomly, pytest-timeout, scipy)
1. `python3 prepare.py`: monta `data/tasks.json` (enunciado EvalPlus, referência, suíte oficial, EvalPlus).
2. `python3 mutate.py`: mutantes de fronteira (ROR, CON, RNG) e genéricos (AOR, LCR, NEG) nas referências.
3. `python3 generate.py claude|openai|deepseek 3`: 3 gerações por tarefa e modelo, via API,
   temperatura padrão. Chaves e modelos só por variável de ambiente (`*_API_KEY`, `*_MODEL`).
4. `python3 extract.py`: extrai e congela o código das respostas.
5. `K=10 python3 run.py`: executa as três suítes K vezes por sujeito (processo novo,
   PYTHONHASHSEED aleatório, ordem dos testes embaralhada, timeout de 10 s).
6. `python3 analyze_mutants.py`: mutation score por suíte e por grupo de operador.

Dados de origem: HumanEval (OpenAI), MBPP sanitizado (Google), HumanEval+ v0.1.10 e MBPP+ v0.2.0 (EvalPlus).

## Registro das gerações (09/11/2026)
- Modelos: `claude-opus-5-5` (Anthropic), `gpt-6.1-sol` (OpenAI), `deepseek-v4-pro` (DeepSeek); 30 tarefas × 3 gerações cada; temperatura e esforço de raciocínio padrão.
- Limite de saída: 16.384 tokens. As 3 respostas do DeepSeek para Mbpp/239 estouraram esse limite só com raciocínio
  (sem código) e foram refeitas com 65.536 tokens; as respostas truncadas originais ficam em `raw_truncados/`.
