from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[76.207292,12.332817],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_kuv_05020+1216/sdB_kuv_05020+1216_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_kuv_05020+1216/sdB_kuv_05020+1216_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
