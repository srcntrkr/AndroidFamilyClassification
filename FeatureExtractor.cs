namespace StatikFeatureExtractor
{
    public class Program
    {
        public static void Main(string[] args)
        {
            StreamReader apisReader = new StreamReader(@"D:\Study\bestApiCallFeatures.txt");
            StreamReader permissionsReader = new StreamReader(@"D:\Study\bestPermissionFeatures.txt");

            List<string> permissions = permissionsReader.ReadToEnd().Split(new[] { "\r\n", "\r", "\n" }, StringSplitOptions.None).ToList();
            List<string> apiCalls = apisReader.ReadToEnd().Split(new[] { "\r\n", "\r", "\n" }, StringSplitOptions.None).ToList();

            StreamWriter writer = new StreamWriter(Path.Combine("D:\\Study", "features.txt"));

            foreach (string familyFolder in Directory.GetDirectories(@"D:\Study\ApktoolOutputs"))
            {
                foreach (string malwareFolder in Directory.GetDirectories(familyFolder))
                {
                    string apiCallsFile = Path.Combine(malwareFolder, "apiCalls.txt");
                    string manifestFile = Path.Combine(malwareFolder, "AndroidManifest.xml");

                    StreamReader apiReader = new StreamReader(apiCallsFile);
                    StreamReader manifestReader = new StreamReader(manifestFile);

                    string manifest = manifestReader.ReadToEnd();
                    List<string> apisOfMalware = apiReader.ReadToEnd().Split(new[] { "\r\n", "\r", "\n" }, StringSplitOptions.None).ToList();

                    var match = Regex.Matches(manifest, "<uses-permission.*").Cast<Match>().ToList();

                    foreach (string permission in permissions)
                    {
                        writer.Write(match.Count(i => i.Value.Contains("\"" + permission + "\"")) > 0 ? "1," : "0,");
                    }

                    foreach (string apiCall in apiCalls)
                    {
                        writer.Write(apisOfMalware.Contains(apiCall) ? "1," : "0,");
                    }

                    writer.Write(Path.GetFileName(familyFolder));
                    writer.Write(writer.NewLine);

                    apiReader.Close();
                    manifestReader.Close();

                }
            }

            permissionsReader.Close();
            apisReader.Close();
            writer.Close();
		}
	}
}