from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[141.68725,38.807281],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_KUV_09236+3901/sdB_KUV_09236+3901_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_KUV_09236+3901/sdB_KUV_09236+3901_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
