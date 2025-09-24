# Bu operatörler iki değeri karşılaştırmak için kullanılır.
"""
ör; ==(eşit mi) => 5==5 sonuç:True
    !=(eşit değil mi) => 5 != 5 sonuç:False
    < (küçük mü) => 3<3 sonuç:false
    > (büyük mü) => 3>2 sonuç:true
    >= (büyük veya eşti mi) => 3>=3 sonuç:false (bir yerde veya, ya da ifadesi geçiyorsa en az bir tanesinin sağlanması durumunda sonuç true olur, eğer her ikisi de sağlanmıyorsa o zaman sonuç false olur.)
    <= (küçük veya eşit mi) => 5 <= 4 sonuç:false(her iki durumda false olduğu için sonuç yine false olur.)

    and (ve) => true and false =  false
    or (veya,ya da) => true or false = true
    not (değil) => not true = false
"""
print(5>2 and 3 > 2) # sonuç: true (çünkü her iki durumu da sağlıyor)
#Not: and operatörü => her iki koşul eğer true ise sonuç true, eğer her iki koşul false ise sonuç false, eğer en az bir tanesi false ise sonuç false olur.

print(3<5 and 8>10) # sonuç:false
print(3<5 or 8>10) # sonuç:true
print(not(5>2)) # sonuç:false
