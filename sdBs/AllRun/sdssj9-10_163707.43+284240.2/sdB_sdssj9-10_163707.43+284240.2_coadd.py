from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[249.280958,28.711167],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj9-10_163707.43+284240.2/sdB_sdssj9-10_163707.43+284240.2_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj9-10_163707.43+284240.2/sdB_sdssj9-10_163707.43+284240.2_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
