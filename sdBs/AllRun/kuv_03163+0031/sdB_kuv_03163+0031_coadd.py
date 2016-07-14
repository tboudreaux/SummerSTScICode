from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[49.725458,0.693081],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_kuv_03163+0031/sdB_kuv_03163+0031_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_kuv_03163+0031/sdB_kuv_03163+0031_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
