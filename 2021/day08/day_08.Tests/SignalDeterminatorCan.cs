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
        public void Count_Number_Of_Times_A_Specific_Signal_Length_Appears_In_The_Given_Input()
        {
            var decoder = new SignalDeterminator();
            decoder.Input = _input;
            var count = decoder.DecodeByLength(s => s is 2 or 3 or 4 or 7);

            Assert.AreEqual(26, count);
        }

        [Test]
        public void Blabla()
        {
            var decoder = new SignalDeterminator();
            decoder.Input = _input;
            var count = decoder.Decode().Sum();

            Assert.AreEqual(61229, count);
        }
    }
}