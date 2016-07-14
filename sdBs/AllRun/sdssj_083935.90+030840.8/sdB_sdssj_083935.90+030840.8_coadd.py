from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[129.899583,3.144667],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_083935.90+030840.8/sdB_sdssj_083935.90+030840.8_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_083935.90+030840.8/sdB_sdssj_083935.90+030840.8_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
