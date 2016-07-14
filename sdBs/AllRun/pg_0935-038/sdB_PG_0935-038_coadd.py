from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[144.543292,-3.999625],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_PG_0935-038/sdB_PG_0935-038_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_PG_0935-038/sdB_PG_0935-038_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()