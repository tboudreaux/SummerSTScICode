from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[47.370167,-2.549931],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_kuv_03070-0244/sdB_kuv_03070-0244_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_kuv_03070-0244/sdB_kuv_03070-0244_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
