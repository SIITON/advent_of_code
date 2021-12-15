using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace day_15
{
    public class PathFinder
    {
        private List<int[]> data;
        private Dictionary<int[], int> pathRisk;
        public List<string> Input { get; set; }

        public int GetPathWithLowestRisk()
        {
            data = Input.Select(line => line.AsEnumerable().Select(p => int.Parse(p.ToString())).ToArray()).ToList();

            pathRisk = new Dictionary<int[], int>(new IntArrayEqualityComparer()); // Path -> risk

            return RiskOfPoint(new []{0, 0}) - data[0][0];
        }


        /*  start
         *      +-----> y
         *      |
         *      |
         *      V     * 
         *      x       goal
         */
        public int RiskOfPoint(int[] pos) // [x, y]
        {
            if (pathRisk.ContainsKey(pos))
            {
                return pathRisk[pos];
            }
            if (pos.IsOutOfBoundsGiven(Input))
            {
                return int.MaxValue;
            }

            if (pos.IsAtGoalGiven(Input))
            {
                return data[pos[0]][pos[1]];
            }
            // move down, or move right. Choose min risk.
            var risk = data[pos[0]][pos[1]] + Math.Min(
                RiskOfPoint(new[] { pos[0] + 1, pos[1] }), 
                RiskOfPoint(new[] { pos[0], pos[1] + 1 }));

            pathRisk.Add(pos, risk);
            return risk;
        }
    }

    public static class Extensions
    {
        public static bool IsOutOfBoundsGiven(this int[] pos, List<string> input)
        {
            return pos[0] < 0 || pos[0] >= input.Count || pos[1] < 0 || pos[1] >= input[0].Length;
        }

        public static bool IsAtGoalGiven(this int[] pos, List<string> input)
        {
            return pos[0] == input.Count - 1 && pos[1] == input[0].Length - 1;
        }
    }
}
