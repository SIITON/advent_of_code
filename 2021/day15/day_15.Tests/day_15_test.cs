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
            finder.ParseInput();
        }

        [Test]
        public void Can_Solve_Part_1()
        {
            var riskLevel = finder.GetPathWithLowestRisk();
            Assert.AreEqual(40, riskLevel);
        }

        [Test]
        public void Can_Solve_Part_2_by_expanding_input()
        {
            finder.ExpandInputSpace();
            var riskLevel = finder.GetPathWithLowestRisk();
            Assert.AreEqual(315, riskLevel);
        }
        [Test]
        public void Can_Solve_Part_2_with_expanded_input()
        {
            finder.Input = File.ReadAllLines(
                "C:\\Users\\simon.tonnes\\source\\repos\\advent_of_code\\day15\\day_15.Tests\\testinput2.txt").ToList();
            finder.ParseInput();
            var riskLevel = finder.GetPathWithLowestRisk();
            Assert.AreEqual(315, riskLevel);
        }

        [Test]
        public void Can_Expand_Input_Space()
        {
            var compare = File.ReadAllLines(
                "C:\\Users\\simon.tonnes\\source\\repos\\advent_of_code\\day15\\day_15.Tests\\testinput2.txt").ToList();
            finder.ExpandInputSpace();
            var data = finder.data;

            var compareData = compare.Select(line => line.AsEnumerable().Select(p => int.Parse(p.ToString())).ToArray()).ToList();

            for (int i = 0; i < data.Count; i++)
            {
                Assert.AreEqual(compareData[i], data[i], $"row num {i} differs.");
            }

        }
    }
}