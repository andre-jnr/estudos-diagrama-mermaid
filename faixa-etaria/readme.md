# Faixa etária

Programa que ler qualquer idade e retorna a faixa etária daquela idade.

## Fluxograma

```mermaid
  graph LR;
      A([Inicio]) --> B[Idade];
      B --> C{idade < 12};
      C -->|Sim| D[/Criança/];
      C -->|Não| E{idade < 18};
      E -->|Sim| F[/Adolescente/];
      E -->|Não| G{idade < 30};
      G -->|Sim| H[/Jovem/];
      G -->|Não| I{Idade < 60};
      I -->|Sim| J[/Adulto/];
      I -->|Não| K[/Idoso/];
      K --> L([Fim]) 
```
