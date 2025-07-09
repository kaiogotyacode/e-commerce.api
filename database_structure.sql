-- Script SQL para criar tabelas com campos de auditoria padrão
-- Baseado na estrutura do BaseModel

-- ============================================================================
-- TABELA DE USUÁRIOS (exemplo atualizado)
-- ============================================================================
CREATE TABLE usuario.tbl_usuario (
    -- Chave primária
    id SERIAL PRIMARY KEY,
    
    -- Campos específicos do usuário
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL,
    
    -- Campos de auditoria (herdados do BaseModel)
    u_inclusao INTEGER,                    -- ID do usuário que incluiu
    inclusao TIMESTAMP DEFAULT NOW(),     -- Data/hora da inclusão
    u_alteracao INTEGER,                   -- ID do usuário que fez a última alteração
    alteracao TIMESTAMP                    -- Data/hora da última alteração
);

-- Índices para melhor performance nas consultas de auditoria
CREATE INDEX idx_usuario_u_inclusao ON usuario.tbl_usuario(u_inclusao);
CREATE INDEX idx_usuario_inclusao ON usuario.tbl_usuario(inclusao);
CREATE INDEX idx_usuario_u_alteracao ON usuario.tbl_usuario(u_alteracao);

-- ============================================================================
-- TEMPLATE PARA NOVAS TABELAS
-- ============================================================================
-- Substitua 'schema_name' e 'tbl_nome' pelos valores corretos
-- Adicione seus campos específicos na seção indicada

CREATE TABLE schema_name.tbl_nome (
    -- Chave primária (obrigatório)
    id SERIAL PRIMARY KEY,
    
    -- ========================================================================
    -- SEUS CAMPOS ESPECÍFICOS AQUI
    -- ========================================================================
    -- campo1 VARCHAR(255) NOT NULL,
    -- campo2 INTEGER,
    -- campo3 DECIMAL(10,2),
    -- campo4 BOOLEAN DEFAULT FALSE,
    -- campo5 TEXT,
    
    -- ========================================================================
    -- CAMPOS DE AUDITORIA PADRÃO (NÃO ALTERAR)
    -- ========================================================================
    u_inclusao INTEGER,                    -- ID do usuário que incluiu
    inclusao TIMESTAMP DEFAULT NOW(),     -- Data/hora da inclusão
    u_alteracao INTEGER,                   -- ID do usuário que fez a última alteração
    alteracao TIMESTAMP                    -- Data/hora da última alteração
);

-- Índices padrão para auditoria (recomendado para todas as tabelas)
CREATE INDEX idx_nome_u_inclusao ON schema_name.tbl_nome(u_inclusao);
CREATE INDEX idx_nome_inclusao ON schema_name.tbl_nome(inclusao);
CREATE INDEX idx_nome_u_alteracao ON schema_name.tbl_nome(u_alteracao);

-- ============================================================================
-- EXEMPLO: TABELA DE PRODUTOS
-- ============================================================================
CREATE TABLE loja.tbl_produto (
    -- Chave primária
    id SERIAL PRIMARY KEY,
    
    -- Campos específicos do produto
    nome VARCHAR(255) NOT NULL,
    preco DECIMAL(10,2) NOT NULL,
    categoria_id INTEGER NOT NULL,
    descricao TEXT,
    ativo BOOLEAN DEFAULT TRUE,
    
    -- Campos de auditoria padrão
    u_inclusao INTEGER,
    inclusao TIMESTAMP DEFAULT NOW(),
    u_alteracao INTEGER,
    alteracao TIMESTAMP,
    
    -- Chaves estrangeiras
    FOREIGN KEY (categoria_id) REFERENCES loja.tbl_categoria(id)
);

-- Índices para a tabela de produtos
CREATE INDEX idx_produto_categoria ON loja.tbl_produto(categoria_id);
CREATE INDEX idx_produto_nome ON loja.tbl_produto(nome);
CREATE INDEX idx_produto_u_inclusao ON loja.tbl_produto(u_inclusao);
CREATE INDEX idx_produto_inclusao ON loja.tbl_produto(inclusao);
CREATE INDEX idx_produto_u_alteracao ON loja.tbl_produto(u_alteracao);

-- ============================================================================
-- TRIGGERS PARA AUDITORIA AUTOMÁTICA (OPCIONAL)
-- ============================================================================
-- Função para atualizar automaticamente o campo 'alteracao'
CREATE OR REPLACE FUNCTION atualizar_timestamp_alteracao()
RETURNS TRIGGER AS $$
BEGIN
    NEW.alteracao = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Trigger para a tabela de usuários
CREATE TRIGGER tr_usuario_atualizar_alteracao
    BEFORE UPDATE ON usuario.tbl_usuario
    FOR EACH ROW
    EXECUTE FUNCTION atualizar_timestamp_alteracao();

-- Trigger para a tabela de produtos (exemplo)
CREATE TRIGGER tr_produto_atualizar_alteracao
    BEFORE UPDATE ON loja.tbl_produto
    FOR EACH ROW
    EXECUTE FUNCTION atualizar_timestamp_alteracao();

-- ============================================================================
-- CONSULTAS ÚTEIS PARA AUDITORIA
-- ============================================================================

-- Ver histórico de inclusões por usuário
SELECT 
    u.nome as usuario_incluiu,
    COUNT(*) as total_inclusoes
FROM usuario.tbl_usuario t
JOIN usuario.tbl_usuario u ON t.u_inclusao = u.id
GROUP BY u.id, u.nome
ORDER BY total_inclusoes DESC;

-- Ver registros alterados nas últimas 24 horas
SELECT *
FROM usuario.tbl_usuario
WHERE alteracao >= NOW() - INTERVAL '24 hours'
ORDER BY alteracao DESC;

-- Ver registros nunca alterados (apenas incluídos)
SELECT *
FROM usuario.tbl_usuario
WHERE alteracao IS NULL
ORDER BY inclusao DESC;
