from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[42.599667,-4.103369],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_PB_9286/sdB_PB_9286_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_PB_9286/sdB_PB_9286_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
