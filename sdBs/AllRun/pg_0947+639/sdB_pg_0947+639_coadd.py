from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[147.908417,63.760331],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_0947+639/sdB_pg_0947+639_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_0947+639/sdB_pg_0947+639_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
