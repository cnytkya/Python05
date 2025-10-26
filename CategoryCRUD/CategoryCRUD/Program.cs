using CategoryCRUD.Data;
using CategoryCRUD.Models;
using Microsoft.EntityFrameworkCore;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddControllersWithViews();

//DI(Dipendency Injection - baðýmlýlýk enjeksiyonu)
builder.Services.AddDbContext<AppDbContext>(opt=>opt.UseSqlServer(builder.Configuration.GetConnectionString("DefaultConnection")));

var app = builder.Build();
// Uygulama baþlarken veritabanýný örnek verilerle doldur (opsiyonel ama önerilir)
SeedDatabase(app);

// Configure the HTTP request pipeline.
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Home/Error");
    // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseRouting();

app.UseAuthorization();

app.MapStaticAssets();

app.MapControllerRoute(
    name: "default",
    pattern: "{controller=Home}/{action=Index}/{id?}")
    .WithStaticAssets();


app.Run();

// Veritabanýný örnek verilerle doldurmak için yardýmcý metot
static void SeedDatabase(IHost app)
{
    using (var scope = app.Services.CreateScope())
    {
        var services = scope.ServiceProvider;
        try
        {
            var context = services.GetRequiredService<AppDbContext>();

            // Veritabanýnýn oluþturulduðundan emin ol (In-Memory için hýzlýdýr)
            context.Database.EnsureCreated();

            // Eðer hiç kategori yoksa, birkaç tane ekle
            if (!context.Categories.Any())
            {
                context.Categories.AddRange(
                    new Category { Name = "Elektronik" },
                    new Category { Name = "Kitap" },
                    new Category { Name = "Giyim" },
                    new Category { Name = "Technology"}
                );
                context.SaveChanges();
            }
        }
        catch (Exception ex)
        {
            var logger = services.GetRequiredService<ILogger<Program>>();
            logger.LogError(ex, "Veritabaný seed iþlemi sýrasýnda bir hata oluþtu.");
        }
    }
}
