using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace day_07
{
    public class CrabSubmarines
    {
        private List<int> _horizontalPositions;

        public void SetHorizontalPositions(string filePath)
        {
            var input = File.ReadAllText(filePath)
                .Split(",")
                .ToList();
            var horizontalPositions = new List<int>();
            foreach (var number in input)
            {
                horizontalPositions.Add(int.Parse(number));
            }

            _horizontalPositions = horizontalPositions;
        }

        public void SetHorizontalPositions(List<int> horizontalPositions)
        {
            _horizontalPositions = horizontalPositions;
        }

        public int GetLowestFuelCostWhenAligned()
        {
            var fuelCosts = new List<int>();
            for (int target = 0; target < _horizontalPositions.Max() / 2; target++)
            {
                var distances = new List<int>();
                foreach (var pos in _horizontalPositions)
                {
                    distances.Add(Math.Abs(pos - target));
                }
                fuelCosts.Add(distances.Sum());
            }

            return fuelCosts.Min();
        }

        public int GetTheActualLowestFuelCostWhenAligned()
        {
            var fuelCosts = new List<int>();
            for (int target = 0; target < _horizontalPositions.Max() / 2; target++)
            {
                var distances = new List<int>();
                foreach (var pos in _horizontalPositions)
                {
                    distances.Add(Math.Abs(pos - target));
                }

                var fuelCost = 0;
                foreach (var distance in distances)
                {
                    fuelCost += DistanceToFuel(distance);
                }
                fuelCosts.Add(fuelCost);
            }

            return fuelCosts.Min();
        }

        private int DistanceToFuel(int d)
        {
            return (d % 2 == 0) ? (d + 1) * (d / 2) : d + d * ((d-1) / 2);
        }
    }
}
