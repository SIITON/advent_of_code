using System;
using System.IO;

namespace day_16
{
    class Program
    {
        static void Main(string[] args)
        {
            var hexInput = File.ReadAllText("C:\\Users\\simon.tonnes\\source\\repos\\advent_of_code\\day16\\day_16\\input.txt");

            var decoder = new PacketDecoder();
            var binary = decoder.ParseToBinary(hexInput);
            Console.WriteLine(binary);
        }
    }
}
