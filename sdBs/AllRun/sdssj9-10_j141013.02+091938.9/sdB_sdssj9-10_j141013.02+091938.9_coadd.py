from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[212.55425,9.327472],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj9-10_j141013.02+091938.9/sdB_sdssj9-10_j141013.02+091938.9_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj9-10_j141013.02+091938.9/sdB_sdssj9-10_j141013.02+091938.9_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()