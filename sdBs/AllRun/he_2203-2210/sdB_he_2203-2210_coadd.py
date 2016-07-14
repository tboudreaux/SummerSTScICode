from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[331.622417,-21.933333],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_he_2203-2210/sdB_he_2203-2210_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_he_2203-2210/sdB_he_2203-2210_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
