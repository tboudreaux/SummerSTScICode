from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[174.356583,5.264083],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj9-10_113725.58+051550.7/sdB_sdssj9-10_113725.58+051550.7_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj9-10_113725.58+051550.7/sdB_sdssj9-10_113725.58+051550.7_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
