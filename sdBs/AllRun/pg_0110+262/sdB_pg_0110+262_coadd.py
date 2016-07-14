from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[18.312,26.458653],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_0110+262/sdB_pg_0110+262_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_0110+262/sdB_pg_0110+262_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
