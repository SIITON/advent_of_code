using System.Collections.Generic;
using System.IO;
using System.Linq;
using NUnit.Framework;

namespace day_15.Tests
{
    public class Tests
    {
        private List<string> input;
        private PathFinder finder;

        [SetUp]
        public void Setup()
        {
            input = File.ReadAllLines(
                "C:\\Users\\simon.tonnes\\source\\repos\\advent_of_code\\day15\\day_15.Tests\\testinput.txt").ToList();
            finder = new PathFinder();
            finder.Input = input;
        }

        [Test]
        public void Can_Solve_Part_1()
        {
            var riskLevel = finder.GetPathWithLowestRisk();
            Assert.AreEqual(40, riskLevel);
        }
    }
}