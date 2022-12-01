using System.Collections.Generic;
using NUnit.Framework;

namespace day_07.Tests
{
    public class CrabSubmarinesCan
    {
        private CrabSubmarines _crabSubs;

        [SetUp]
        public void Setup()
        {
            _crabSubs = new CrabSubmarines();
        }

        [Test]
        public void Estimate_The_Lowest_Fuel_Cost_To_Align_Crabs_When_Given_Horizontal_Positions()
        {
            // Assign
            var horizontalPositions = new List<int>() { 16, 1, 2, 0, 4, 2, 7, 1, 2, 14 };
            _crabSubs.SetHorizontalPositions(horizontalPositions);
            // Act
            var fuelCost = _crabSubs.GetLowestFuelCostWhenAligned();
            // Assert
            Assert.AreEqual(37, fuelCost);
        }

        [Test]
        public void Determine_The_Actual_Fuel_Cost_To_Align_Crabs_When_Given_Horizontal_Positions()
        {
            // Assign
            var horizontalPositions = new List<int>() { 16, 1, 2, 0, 4, 2, 7, 1, 2, 14 };
            _crabSubs.SetHorizontalPositions(horizontalPositions);
            // Act
            var fuelCost = _crabSubs.GetTheActualLowestFuelCostWhenAligned();
            // Assert
            Assert.AreEqual(168, fuelCost);
        }
    }
}