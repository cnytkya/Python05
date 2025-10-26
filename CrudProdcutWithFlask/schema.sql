--işlem yapmak istediğimiz veritabanına geçiş yapıyoruz
use CategoryCRUD

-- Bu komut, 'products' adında bir tablo yoksa onu oluşturur.
-- 'id' sütunu birincil anahtardır ve her yeni kayıtta otomatik artar.
-- 'name' ve 'price' sütunlarının boş olmasına izin verilmez (NOT NULL).
CREATE TABLE Products (
    Id INT PRIMARY KEY IDENTITY(1,1),
    Name NVARCHAR(255) NOT NULL,
    Price DECIMAL(10, 2) NOT NULL
);

--yeni ürün oluşturma
INSERT INTO Products (name, Price, CategoryId)
VALUES (N'Oyuncu Klavyesi', 1250.75, 1);

--bütün ürünleri listele
SELECT * FROM Products

--category id si 1 olan bütün ürünleri listele
SELECT * FROM Products
WHERE CategoryId = 1;

--id si 2 olan ürünü silelim
DELETE FROM Products
WHERE Id = 2;

--bir ürünü güncelleme
UPDATE Products
SET 
    name = N'Tablet',
    Price = 3200.50
WHERE 
    Id = 3;
