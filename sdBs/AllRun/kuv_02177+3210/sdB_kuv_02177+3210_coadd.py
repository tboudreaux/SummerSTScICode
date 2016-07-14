from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[35.166292,32.39585],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_kuv_02177+3210/sdB_kuv_02177+3210_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_kuv_02177+3210/sdB_kuv_02177+3210_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
