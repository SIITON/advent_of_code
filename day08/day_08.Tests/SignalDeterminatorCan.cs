using System.Collections.Generic;
using System.IO;
using System.Linq;
using NUnit.Framework;

namespace day_08.Tests
{
    public class SignalDeterminatorCan
    {
        private List<string> _input;

        [SetUp]
        public void Setup()
        {
            _input = File.ReadAllLines("C:\\Users\\simon.tonnes\\source\\repos\\advent_of_code\\day08\\day_08.Tests\\testdata.txt").ToList();
        }

        [Test]
        public void Decode_Signal_Correct_When_Given_Input()
        {
            var decoder = new SignalDeterminator();
            decoder.Input = _input;
            var count = decoder.Decode(s => s is 2 or 3 or 4 or 7);

            Assert.AreEqual(26, count);
        }
    }
}