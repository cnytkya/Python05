using CategoryCRUD.Data;
using CategoryCRUD.Models;
using Microsoft.EntityFrameworkCore;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddControllersWithViews();

//DI(Dipendency Injection - ba��ml�l�k enjeksiyonu)
builder.Services.AddDbContext<AppDbContext>(opt=>opt.UseSqlServer(builder.Configuration.GetConnectionString("DefaultConnection")));

var app = builder.Build();
// Uygulama ba�larken veritaban�n� �rnek verilerle doldur (opsiyonel ama �nerilir)
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

// Veritaban�n� �rnek verilerle doldurmak i�in yard�mc� metot
static void SeedDatabase(IHost app)
{
    using (var scope = app.Services.CreateScope())
    {
        var services = scope.ServiceProvider;
        try
        {
            var context = services.GetRequiredService<AppDbContext>();

            // Veritaban�n�n olu�turuldu�undan emin ol (In-Memory i�in h�zl�d�r)
            context.Database.EnsureCreated();

            // E�er hi� kategori yoksa, birka� tane ekle
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
            logger.LogError(ex, "Veritaban� seed i�lemi s�ras�nda bir hata olu�tu.");
        }
    }
}
