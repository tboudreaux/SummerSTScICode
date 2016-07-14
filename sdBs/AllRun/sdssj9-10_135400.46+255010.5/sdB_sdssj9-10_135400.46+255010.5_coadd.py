from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[208.501917,25.83625],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj9-10_135400.46+255010.5/sdB_sdssj9-10_135400.46+255010.5_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj9-10_135400.46+255010.5/sdB_sdssj9-10_135400.46+255010.5_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
