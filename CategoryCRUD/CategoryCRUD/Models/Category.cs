using System.ComponentModel.DataAnnotations;

namespace CategoryCRUD.Models
{
    public class Category
    {
        //public Guid Id { get; set; } id string olacak.
        //aşağıdakiler Category modelinin 
        public int Id { get; set; } //uniq yani benzersiz kimlik(id). primary key(her kayıt için benzersiz bir kimlik atayacak ve 1,1 artacak şekilde...)

        [Required(ErrorMessage = "Kategori adı zorunludur.")]
        [StringLength(100, ErrorMessage = "Kategori adı en fazla 100 karakter olabilir.")]
        [Display(Name = "Kategori Adı")]
        public string Name { get; set; }
    }
}
