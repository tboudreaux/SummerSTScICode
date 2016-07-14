from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[20.930042,-5.095908],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_PB_8783/sdB_PB_8783_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_PB_8783/sdB_PB_8783_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
