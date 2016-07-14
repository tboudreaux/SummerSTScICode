from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[234.203458,68.869067],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1536+690/sdB_pg_1536+690_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1536+690/sdB_pg_1536+690_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
