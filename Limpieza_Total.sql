-- ============================================================================
-- LIMPIEZA TOTAL - TRABAJO GRUPO PAU
-- BD II - ETSI Informatica - Universidad de Malaga
--
-- EJECUTAR COMO SYS
-- Elimina TODO: usuarios dinámicos, roles, VPD, auditoría, objetos PAU,
-- el usuario PAU, y los tablespaces.
-- ============================================================================

SET SERVEROUTPUT ON SIZE UNLIMITED
SET LINESIZE 200

PROMPT ========================================
PROMPT 1. DROP AUDIT POLICY
PROMPT ========================================
BEGIN
  EXECUTE IMMEDIATE 'NOAUDIT POLICY audit_asistencia_updates';
EXCEPTION WHEN OTHERS THEN NULL;
END;
/
BEGIN
  EXECUTE IMMEDIATE 'DROP AUDIT POLICY audit_asistencia_updates';
EXCEPTION WHEN OTHERS THEN NULL;
END;
/

PROMPT ========================================
PROMPT 2. DROP VPD POLICY
PROMPT ========================================
BEGIN
  DBMS_RLS.DROP_POLICY(
    object_schema => 'PAU',
    object_name   => 'ESTUDIANTE',
    policy_name   => 'POL_ESTUDIANTE_VPD'
  );
EXCEPTION WHEN OTHERS THEN NULL;
END;
/

PROMPT ========================================
PROMPT 3. DROP USERS CREADOS DINAMICAMENTE (EST_*, VOC_*)
PROMPT ========================================
BEGIN
  FOR rec IN (SELECT username FROM dba_users 
              WHERE username LIKE 'EST_%' OR username LIKE 'VOC_%') LOOP
    BEGIN
      FOR s IN (SELECT sid, serial# FROM v$session 
                WHERE username = rec.username) LOOP
        EXECUTE IMMEDIATE 'ALTER SYSTEM KILL SESSION ''' || s.sid || ',' || s.serial# || ''' IMMEDIATE';
      END LOOP;
    EXCEPTION WHEN OTHERS THEN NULL;
    END;
    BEGIN
      EXECUTE IMMEDIATE 'DROP USER ' || rec.username || ' CASCADE';
      DBMS_OUTPUT.PUT_LINE('Usuario ' || rec.username || ' eliminado');
    EXCEPTION WHEN OTHERS THEN NULL;
    END;
  END LOOP;
END;
/

PROMPT ========================================
PROMPT 4. DROP ROLES
PROMPT ========================================
BEGIN
  FOR rec IN (SELECT role FROM dba_roles 
              WHERE role IN ('ROL_ESTUDIANTE','ROL_VOCAL','ROL_ACCESO')) LOOP
    BEGIN
      EXECUTE IMMEDIATE 'DROP ROLE ' || rec.role;
      DBMS_OUTPUT.PUT_LINE('Rol ' || rec.role || ' eliminado');
    EXCEPTION WHEN OTHERS THEN NULL;
    END;
  END LOOP;
END;
/

PROMPT ========================================
PROMPT 5. DROP OBJETOS DE PAU (MV, SYNONYM, PROC, PKG, TRIGGER, VIEW)
PROMPT ========================================
BEGIN
  FOR rec IN (SELECT mview_name FROM all_mviews WHERE owner = 'PAU') LOOP
    BEGIN
      EXECUTE IMMEDIATE 'DROP MATERIALIZED VIEW PAU.' || rec.mview_name;
    EXCEPTION WHEN OTHERS THEN NULL;
    END;
  END LOOP;
END;
/

BEGIN
  FOR rec IN (SELECT synonym_name FROM dba_synonyms 
              WHERE owner = 'PUBLIC' AND table_owner = 'PAU') LOOP
    BEGIN
      EXECUTE IMMEDIATE 'DROP PUBLIC SYNONYM ' || rec.synonym_name;
    EXCEPTION WHEN OTHERS THEN NULL;
    END;
  END LOOP;
END;
/

BEGIN
  FOR rec IN (SELECT object_name, object_type FROM dba_objects 
              WHERE owner = 'PAU' 
                AND object_type IN ('PROCEDURE','PACKAGE','PACKAGE BODY',
                                    'FUNCTION','TRIGGER','VIEW')) LOOP
    BEGIN
      EXECUTE IMMEDIATE 'DROP ' || rec.object_type || ' PAU.' || rec.object_name;
    EXCEPTION WHEN OTHERS THEN NULL;
    END;
  END LOOP;
END;
/

PROMPT ========================================
PROMPT 6. DROP TABLAS DE PAU (CONSTRAINTS CASCADE + PURGE)
PROMPT ========================================
BEGIN
  FOR rec IN (SELECT table_name FROM dba_tables 
              WHERE owner = 'PAU' ORDER BY table_name DESC) LOOP
    BEGIN
      EXECUTE IMMEDIATE 'DROP TABLE PAU.' || rec.table_name 
                        || ' CASCADE CONSTRAINTS PURGE';
    EXCEPTION WHEN OTHERS THEN NULL;
    END;
  END LOOP;
END;
/

PROMPT ========================================
PROMPT 7. DROP SEQUENCES DE PAU
PROMPT ========================================
BEGIN
  FOR rec IN (SELECT sequence_name FROM dba_sequences 
              WHERE sequence_owner = 'PAU') LOOP
    BEGIN
      EXECUTE IMMEDIATE 'DROP SEQUENCE PAU.' || rec.sequence_name;
    EXCEPTION WHEN OTHERS THEN NULL;
    END;
  END LOOP;
END;
/

PROMPT ========================================
PROMPT 8. DROP FUNCION VPD (si quedo huerfana)
PROMPT ========================================
BEGIN
  EXECUTE IMMEDIATE 'DROP FUNCTION PAU.FN_ESTUDIANTE_VPD';
EXCEPTION WHEN OTHERS THEN NULL;
END;
/

PROMPT ========================================
PROMPT 9. DROP DIRECTORIO EXTERNO
PROMPT ========================================
BEGIN
  EXECUTE IMMEDIATE 'DROP DIRECTORY directorio_ext';
EXCEPTION WHEN OTHERS THEN NULL;
END;
/

PROMPT ========================================
PROMPT 10. DROP USUARIO PAU (CASCADE para barrer lo que quede)
PROMPT ========================================
BEGIN
  FOR s IN (SELECT sid, serial# FROM v$session WHERE username = 'PAU') LOOP
    EXECUTE IMMEDIATE 'ALTER SYSTEM KILL SESSION ''' || s.sid || ',' || s.serial# || ''' IMMEDIATE';
  END LOOP;
EXCEPTION WHEN OTHERS THEN NULL;
END;
/
BEGIN
  EXECUTE IMMEDIATE 'DROP USER PAU CASCADE';
  DBMS_OUTPUT.PUT_LINE('Usuario PAU eliminado');
EXCEPTION WHEN OTHERS THEN NULL;
END;
/

PROMPT ========================================
PROMPT 11. DROP TABLESPACES (incluyendo datafiles)
PROMPT ========================================
BEGIN
  EXECUTE IMMEDIATE 'DROP TABLESPACE TS_INDICES INCLUDING CONTENTS AND DATAFILES';
  DBMS_OUTPUT.PUT_LINE('Tablespace TS_INDICES eliminado');
EXCEPTION WHEN OTHERS THEN NULL;
END;
/
BEGIN
  EXECUTE IMMEDIATE 'DROP TABLESPACE TS_PAU INCLUDING CONTENTS AND DATAFILES';
  DBMS_OUTPUT.PUT_LINE('Tablespace TS_PAU eliminado');
EXCEPTION WHEN OTHERS THEN NULL;
END;
/

PROMPT ========================================
PROMPT 12. VERIFICACION FINAL - NO DEBEN QUEDAR OBJETOS PAU
PROMPT ========================================
SELECT 'USUARIOS PAU' AS concepto, COUNT(*) AS restante 
FROM dba_users WHERE username LIKE '%PAU%' OR username LIKE 'EST_%' OR username LIKE 'VOC_%'
UNION ALL
SELECT 'ROLES', COUNT(*) FROM dba_roles WHERE role LIKE 'ROL_%'
UNION ALL
SELECT 'TABLESPACES', COUNT(*) FROM dba_tablespaces 
WHERE tablespace_name IN ('TS_PAU','TS_INDICES')
UNION ALL
SELECT 'OBJETOS PAU', COUNT(*) FROM dba_objects WHERE owner = 'PAU';

PROMPT ========================================
PROMPT LIMPIEZA TOTAL COMPLETADA
PROMPT ========================================
