using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Microsoft.Win32.SafeHandles;

namespace day_09
{
    public class Basins
    {
        public char Inner;
        public char Outer;
        private List<string> _data;
        private List<List<bool>> _visited;

        public List<int> FindAllSizes()
        {
            _data = File
                .ReadAllLines("C:\\Users\\simon.tonnes\\source\\repos\\advent_of_code\\day09\\day_09\\preprocessed.txt")
                .ToList();

            var xDiff = new List<int>() { 0, -1, 0, 1 };
            var yDiff = new List<int>() { -1, 0, 1, 0 };
            _visited = InitVisitedStates();
            var basinSizes = new List<int>();
            for (int i = 0; i < _data.Count; i++)
            {
                for (int j = 0; j < _data[0].Length; j++)
                {
                    if (!_visited[i][j] && _data[i][j] == Inner)
                    {
                        var basinSize = GetSize(i, j);
                        basinSizes.Add(basinSize);
                    }
                }
            }

            return basinSizes;
        }

        private List<List<bool>> InitVisitedStates()
        {
            var visited = new List<List<bool>>(100);
            for (int i = 0; i < 100; i++)
            {
                var boolList = Enumerable.Repeat(false, 100).ToList();
                visited.Add(boolList);
            }

            return visited;
        }

        public int GetSize(int x, int y)
        {
            // if visited or out of boundry: return
            if (_visited[x][y] || _data[x][y] == Outer)
            {
                return 0;
            }

            _visited[x][y] = true;
            var size = 1;
            size += (y > 0) ? GetSize(x, y - 1) : 0; // left
            size += (x > 0) ? GetSize(x - 1, y) : 0; // top
            size += (y < _data[0].Length - 1) ? GetSize(x, y + 1) : 0; // right
            size += (x < _data.Count - 1) ? GetSize(x + 1, y) : 0; // bottom

            return size;
        }
    }
}
