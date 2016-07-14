from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[249.059292,53.216306],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1635+533/sdB_pg_1635+533_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1635+533/sdB_pg_1635+533_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
