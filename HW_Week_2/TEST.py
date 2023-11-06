using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Xin chào! Hãy nhập tên của bạn:");

        // Nhập tên từ người dùng
        string name = Console.ReadLine();

        // Hiển thị thông điệp chào mừng
        Console.WriteLine("Xin chào, " + name + "! Chúc bạn một ngày tốt lành!");

        // Dừng chương trình để người dùng có thể đọc thông điệp
        Console.ReadLine();
    }
}