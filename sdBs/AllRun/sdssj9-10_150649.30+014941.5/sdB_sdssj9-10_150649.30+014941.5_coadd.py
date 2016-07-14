from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[226.705417,1.828194],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj9-10_150649.30+014941.5/sdB_sdssj9-10_150649.30+014941.5_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj9-10_150649.30+014941.5/sdB_sdssj9-10_150649.30+014941.5_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
