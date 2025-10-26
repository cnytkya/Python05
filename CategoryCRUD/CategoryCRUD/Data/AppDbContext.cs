using CategoryCRUD.Models;
using Microsoft.EntityFrameworkCore;

namespace CategoryCRUD.Data
{
    public class AppDbContext : DbContext
    {
        public AppDbContext(DbContextOptions<AppDbContext> options) : base(options)
        {
        }

        public DbSet<Category> Categories { get; set; }//veritabındaki tablonun ismi Categories olacak.
    }
}
