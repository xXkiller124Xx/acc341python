-- proof.sql
-- Three INSERT statements that PostgreSQL should refuse, plus the
-- exact error message each one produced when I ran it in Neon.
-- =====================================================================
-- TEST 1: foreign key should refuse a payment_id that does not exist
-- =====================================================================
INSERT INTO payment_application (payment_id, invoice_id, amount_applied, application_data)
VALUES ( 9999 , 1 , 100.00 , CURRENT_DATE ) ;
-- Error message Neon returned:
-- ERROR: insert or update on table "payment_application" violates foreign key constraint "fk_app_payment" (SQLSTATE 23503)

-- =====================================================================
-- TEST 2: check constraint should refuse a negative amount
-- =====================================================================
INSERT INTO payment_application (payment_id, invoice_id, amount_applied, application_data)
VALUES ( 1 , 1 , - 50.00 , CURRENT_DATE ) ;
-- Error message Neon returned:
-- ERROR: new row for relation "payment_application" violates check constraint "payment_application_amount_applied_check" (SQLSTATE 23514)

-- =====================================================================
-- TEST 3: check constraint should refuse an invalid payment_method
-- =====================================================================
INSERT INTO payment (customer_id, payment_date, payment_method, amount_received, reference_number)
VALUES ( 1 , CURRENT_DATE , 'Bitcoin' , 500.00 , 'BTC-TEST-001' ) ;
-- Error message Neon returned:
-- ERROR: new row for relation "payment" violates check constraint "payment_payment_method_check" (SQLSTATE 23514)